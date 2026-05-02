import json
import subprocess
import sys


def test_builds_pdb_ligand_lookup_payload():
    from scripts.bindingdb_lookup import build_payload

    payload = build_payload(
        lookup_type="pdb",
        query="1Q0L",
        cutoff=100,
        identity=92,
        max_items=10,
        save_raw=False,
        raw_output_path=None,
    )

    assert payload == {
        "base_url": "https://bindingdb.org",
        "path": "rest/getLigandsByPDBs",
        "params": {
            "pdb": "1Q0L",
            "cutoff": 100,
            "identity": 92,
            "response": "application/json",
        },
        "max_items": 10,
        "save_raw": False,
    }


def test_builds_smiles_ligand_lookup_payload_with_compact_default():
    from scripts.bindingdb_lookup import build_payload

    payload = build_payload(
        lookup_type="smiles",
        query="CC(=O)OC1=CC=CC=C1C(=O)O",
        cutoff=0.9,
        identity=None,
        max_items=None,
        save_raw=True,
        raw_output_path="data/staging/bindingdb_aspirin.json",
    )

    assert payload["path"] == "rest/getLigandsBySmiles"
    assert payload["params"] == {
        "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
        "cutoff": 0.9,
        "response": "application/json",
    }
    assert payload["max_items"] == 5
    assert payload["save_raw"] is True
    assert payload["raw_output_path"] == "data/staging/bindingdb_aspirin.json"


def test_cli_prints_rest_helper_json(capsys):
    from scripts.bindingdb_lookup import main

    seen_payloads = []

    def fake_execute(payload):
        seen_payloads.append(payload)
        return {"ok": True, "records": [{"monomerid": 123, "target": "Example"}]}

    exit_code = main(["pdb", "1Q0L"], execute_func=fake_execute)

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert output["records"][0]["monomerid"] == 123
    assert seen_payloads[0]["path"] == "rest/getLigandsByPDBs"


def test_cli_help_runs_when_invoked_as_script():
    result = subprocess.run(
        [sys.executable, "scripts/bindingdb_lookup.py", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Run compact BindingDB REST lookups." in result.stdout
