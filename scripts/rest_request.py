#!/usr/bin/env python3
"""Generic compact REST client for imported life-science research skills."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import requests


def error(code: str, message: str, warnings: list[str] | None = None) -> dict[str, Any]:
    return {"ok": False, "error": {"code": code, "message": message}, "warnings": warnings or []}


def _build_url(base_url: str, path: str) -> str:
    if path.startswith(("http://", "https://")):
        return path
    return base_url.rstrip("/") + "/" + path.lstrip("/")


def _service_name(base_url: str) -> str:
    host = base_url.split("://", 1)[-1].split("/", 1)[0]
    return host.replace(".", "-")


def _compact(value: Any, max_items: int, max_depth: int) -> Any:
    if isinstance(value, str):
        return value if len(value) <= 240 else value[:240] + "..."
    if max_depth <= 0:
        return "..." if isinstance(value, (dict, list)) else value
    if isinstance(value, list):
        compacted = [_compact(item, max_items, max_depth - 1) for item in value[:max_items]]
        if len(value) > max_items:
            compacted.append(f"... (+{len(value) - max_items} more)")
        return compacted
    if isinstance(value, dict):
        output: dict[str, Any] = {}
        items = list(value.items())
        for key, item in items[:max_items]:
            output[str(key)] = _compact(item, max_items, max_depth - 1)
        if len(items) > max_items:
            output["_truncated_keys"] = len(items) - max_items
        return output
    return value


def _infer_records(data: Any) -> tuple[str | None, Any]:
    if isinstance(data, list):
        return "$", data
    if isinstance(data, dict):
        for key in ("records", "results", "items", "activities", "molecules", "targets"):
            value = data.get(key)
            if isinstance(value, list):
                return key, value
    return None, data


def _save_raw_output(raw_output: str, raw_output_path: str | None, base_url: str, suffix: str) -> str:
    path = Path(raw_output_path or f"/tmp/{_service_name(base_url)}-raw.{suffix}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(raw_output, encoding="utf-8")
    return str(path)


def execute(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return error("invalid_input", "Input must be one JSON object.")
    base_url = str(payload.get("base_url") or "").strip()
    path = str(payload.get("path") or "").strip()
    if not base_url or not path:
        return error("invalid_input", "`base_url` and `path` are required.")

    method = str(payload.get("method") or "GET").upper()
    params = payload.get("params") or {}
    headers = payload.get("headers") or {}
    max_items = int(payload.get("max_items") or 5)
    max_depth = int(payload.get("max_depth") or 3)
    timeout_sec = int(payload.get("timeout_sec") or 30)
    save_raw = bool(payload.get("save_raw") or False)
    raw_output_path = payload.get("raw_output_path")

    try:
        response = requests.request(
            method,
            _build_url(base_url, path),
            params=params,
            headers=headers,
            json=payload.get("json_body"),
            data=payload.get("form_body"),
            timeout=timeout_sec,
        )
        response.raise_for_status()
        content_type = (response.headers.get("content-type") or "").lower()
        is_json = "json" in content_type or response.text.lstrip().startswith(("{", "["))
        if is_json:
            data = response.json()
            raw_output = json.dumps(data, indent=2)
            saved_path = (
                _save_raw_output(raw_output, raw_output_path, base_url, "json") if save_raw else None
            )
            record_path, target = _infer_records(data)
            output: dict[str, Any] = {
                "ok": True,
                "source": _service_name(base_url),
                "path": path,
                "method": method,
                "status_code": response.status_code,
                "record_path": record_path,
                "raw_output_path": saved_path,
                "warnings": [],
            }
            if isinstance(target, list):
                records = target[:max_items]
                output.update(
                    {
                        "record_count_returned": len(records),
                        "record_count_available": len(target),
                        "truncated": len(records) < len(target),
                        "records": _compact(records, max_items, max_depth),
                    }
                )
            else:
                output["summary"] = _compact(target, max_items, max_depth)
            return output

        saved_path = (
            _save_raw_output(response.text, raw_output_path, base_url, "txt") if save_raw else None
        )
        return {
            "ok": True,
            "source": _service_name(base_url),
            "path": path,
            "method": method,
            "status_code": response.status_code,
            "content_type": content_type,
            "text_head": None if saved_path else response.text[:800],
            "raw_output_path": saved_path,
            "warnings": [],
        }
    except requests.RequestException as exc:
        return error("network_error", f"Request failed: {exc}")
    except ValueError as exc:
        return error("invalid_response", str(exc))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        sys.stdout.write(json.dumps(error("invalid_json", f"Could not parse JSON input: {exc}")))
        return 2
    output = execute(payload)
    sys.stdout.write(json.dumps(output))
    return 0 if output.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
