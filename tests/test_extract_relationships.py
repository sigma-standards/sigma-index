def test_extract_national_adoption_links_from_iso_member_profiles():
    from scripts.extract_relationships import extract_national_adoption_links

    rows = [
        {
            "sigma_id": "NSB-ANSI-US",
            "name_short": "ANSI",
            "name_full": "American National Standards Institute",
            "data_source": "ISO member profile: https://www.iso.org/member/2188.html",
        },
        {
            "sigma_id": "NSB-BIS-IN",
            "name_short": "BIS",
            "name_full": "Bureau of Indian Standards",
            "data_source": "ISO member profile: https://www.iso.org/fr/member/1794.html",
        },
        {
            "sigma_id": "OTHER-ROW",
            "name_short": "Other",
            "name_full": "Other",
            "data_source": "ISO member profile: https://www.iso.org/member/0000.html",
        },
    ]

    relationships = extract_national_adoption_links(rows)

    assert relationships == [
        {
            "from_id": "NSB-ANSI-US",
            "to_id": "GT-ISO-BODY-1947",
            "relationship_type": "national_adoption_of",
            "confidence": "source-confirmed",
            "source_url": "https://www.iso.org/member/2188.html",
            "notes": "ANSI is listed in the ISO member profile source as a national standards body in the ISO ecosystem.",
        },
        {
            "from_id": "NSB-BIS-IN",
            "to_id": "GT-ISO-BODY-1947",
            "relationship_type": "national_adoption_of",
            "confidence": "source-confirmed",
            "source_url": "https://www.iso.org/fr/member/1794.html",
            "notes": "BIS is listed in the ISO member profile source as a national standards body in the ISO ecosystem.",
        },
    ]


def test_extract_national_adoption_links_ignores_untrusted_member_urls():
    from scripts.extract_relationships import extract_national_adoption_links

    relationships = extract_national_adoption_links(
        [
            {
                "sigma_id": "NSB-EXAMPLE",
                "name_short": "Example",
                "data_source": "ISO member profile: https://www.iso.org.evil.example/member/1.html",
            }
        ]
    )

    assert relationships == []
