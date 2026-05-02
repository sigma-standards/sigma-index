import csv


SHEET_URL = "https://docs.google.com/spreadsheets/d/12B83jPjlKSbk9QX8IQjAJylqwby8puiwabHwHoFBj0Q/edit?gid=0#gid=0"


def test_extract_export_url_from_google_sheet_link():
    from scripts.sync_google_sheet import build_export_url, extract_sheet_reference

    sheet_id, gid = extract_sheet_reference(SHEET_URL)

    assert sheet_id == "12B83jPjlKSbk9QX8IQjAJylqwby8puiwabHwHoFBj0Q"
    assert gid == "0"
    assert build_export_url(sheet_id, gid) == (
        "https://docs.google.com/spreadsheets/d/"
        "12B83jPjlKSbk9QX8IQjAJylqwby8puiwabHwHoFBj0Q/export?format=csv&gid=0"
    )


def test_sync_text_writes_master_schema_and_drops_sheet_metadata(tmp_path):
    from scripts.sync_google_sheet import MASTER_FIELDS, write_normalized_csv

    csv_text = (
        "sigma_id,entry_type,meta_layer,domain,sub_domain,name_full,name_short,standard_id,"
        "issuer,issuer_type,governance_layer,geographic_scope,year_published,year_first,status,"
        "mandate,sector_applicability,why_it_matters,key_outputs,official_url,data_source,notes,"
        "related_sigma_ids,llm_enriched,last_updated\n"
        "HL-WHO-IHR-2005,Treaty,Life Sciences & Health,Health & Medical,Global health security,"
        "International Health Regulations,IHR 2005,IHR 2005,World Health Organization,UN Agency,"
        "International,Global,2005,1969,Active,Treaty-binding,Public health authorities,"
        "Core framework,Regulations,https://www.who.int/,Google Sheet test,Seed row,,no,2026-05-02\n"
    )
    output_path = tmp_path / "google_sheet_master.csv"

    count = write_normalized_csv(csv_text, output_path)

    with output_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    assert count == 1
    assert reader.fieldnames == MASTER_FIELDS
    assert rows[0]["sigma_id"] == "HL-WHO-IHR-2005"
    assert "related_sigma_ids" not in rows[0]


def test_header_only_sheet_writes_empty_schema_file(tmp_path):
    from scripts.sync_google_sheet import MASTER_FIELDS, write_normalized_csv

    output_path = tmp_path / "google_sheet_master.csv"
    count = write_normalized_csv(",".join(MASTER_FIELDS) + "\n", output_path)

    with output_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    assert count == 0
    assert reader.fieldnames == MASTER_FIELDS
    assert rows == []
