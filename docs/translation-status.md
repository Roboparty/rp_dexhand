# English Translation Scope

[Home](../README.md) · [Project plans](../PROJECT_PLANS.md)

Upstream baseline: `Roboparty/rp_dexhand` commit `e43fd90970019b093d41c131d3839d375a74f2be`.
Translation date: 2026-10-18.

## Completed in this fork

- English hardware, quick-start, SDK, ROS 2, models, troubleshooting, downloads and maintenance guides.
- English third-party notice, retaining the original licensing boundaries.
- English entry points. The legacy `README.zh-CN.md` path now points to the English README so existing links continue to work; the original Chinese content remains in upstream Git history.
- English explanations of every Chinese filename and workbook-sheet identifier in the resource records, in [the metadata glossary](resource-metadata-english.md).
- [Two research plans and a shared curriculum](../PROJECT_PLANS.md).

Technical API identifiers, commands, pinned upstream revisions, source URLs and checksum records retain their original meanings. Historical upstream validation is attributed to the snapshot; it is not claimed as testing performed for this translation. Repository visibility statements are contextualized to distinguish this public fork from the original private snapshot.

## Preserved identifiers and assets

The two resource JSON files remain byte-for-byte identical to upstream. Chinese original filenames and sheet names are provenance identifiers, with English meanings in the glossary. This preserves exact resource lookup and the original inspection record.

Dimension and pinout drawings contain numeric labels and the RoboParty logo; their original bytes are retained. The product GIF is retained as an upstream demonstration asset. These assets are not engineering redraws.

## Outside the completed translation

- Linked SDK and ROS repositories are separate repositories, not source directories of this fork.
- The 12 external release attachments, including vendor SDK packages, protocol workbook, CAD/model archives, applications and changelog, are not in this Git checkout. Their internal Chinese content has not been translated.
- Feishu pages and upstream release assets retain their own access requirements. Forking Git history does not copy releases or grant access.
- No driver installation, hardware movement, CAD loading or simulation validation was performed.

The translation does not add a license to upstream material or assert rights to redistribute vendor attachments. See [NOTICE](../NOTICE.md).
