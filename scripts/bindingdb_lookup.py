#!/usr/bin/env python3
"""Compact BindingDB lookup wrapper for SIGMA life-science research tasks."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Callable

try:
    from scripts.rest_request import execute
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from rest_request import execute


BINDINGDB_BASE_URL = "https://bindingdb.org"
LOOKUP_CONFIG = {
    "pdb": ("rest/getLigandsByPDBs", "pdb", 10),
    "uniprot": ("rest/getLigandsByUniprots", "uniprot", 10),
    "smiles": ("rest/getLigandsBySmiles", "smiles", 5),
    "compound": ("rest/getTargetsByCompound", "compound", 10),
}


def build_payload(
    *,
    lookup_type: str,
    query: str,
    cutoff: int | float | None,
    identity: int | None,
    max_items: int | None,
    save_raw: bool,
    raw_output_path: str | None,
) -> dict[str, Any]:
    path, query_param, default_max_items = LOOKUP_CONFIG[lookup_type]
    params: dict[str, Any] = {query_param: query, "response": "application/json"}
    if cutoff is not None:
        params["cutoff"] = cutoff
    if identity is not None:
        params["identity"] = identity

    payload: dict[str, Any] = {
        "base_url": BINDINGDB_BASE_URL,
        "path": path,
        "params": params,
        "max_items": max_items or default_max_items,
        "save_raw": save_raw,
    }
    if raw_output_path:
        payload["raw_output_path"] = raw_output_path
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run compact BindingDB REST lookups.")
    parser.add_argument("lookup_type", choices=sorted(LOOKUP_CONFIG))
    parser.add_argument("query", help="PDB ID, UniProt accession, SMILES string, or compound ID.")
    parser.add_argument("--cutoff", type=float, help="BindingDB endpoint cutoff parameter.")
    parser.add_argument("--identity", type=int, help="Sequence identity threshold for PDB lookups.")
    parser.add_argument("--max-items", type=int, help="Maximum records to include in compact output.")
    parser.add_argument("--save-raw", action="store_true", help="Persist the raw response payload.")
    parser.add_argument("--raw-output-path", help="Path for --save-raw output.")
    return parser


def main(
    argv: list[str] | None = None,
    *,
    execute_func: Callable[[Any], dict[str, Any]] = execute,
) -> int:
    args = build_parser().parse_args(argv)
    payload = build_payload(
        lookup_type=args.lookup_type,
        query=args.query,
        cutoff=args.cutoff,
        identity=args.identity,
        max_items=args.max_items,
        save_raw=args.save_raw,
        raw_output_path=args.raw_output_path,
    )
    output = execute_func(payload)
    sys.stdout.write(json.dumps(output, indent=2, sort_keys=True))
    sys.stdout.write("\n")
    return 0 if output.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
