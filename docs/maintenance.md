# Sources and Maintenance

[Home](../README.md)

## Baseline

Resource snapshot: 2026-10-05. The repository is `rp_dexhand`, the product is RP Hand and the maintained SDK is `roboparty_dexhand`. The upstream record describes completed resource entry points and a versioned archive of 12 original attachments. Joint mapping, public-release licensing and complete ROS-stack acceptance remain outstanding.

| Source | Version | Used for |
| --- | --- | --- |
| [RP Hand user manual](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb) | revision 13 | Specifications, hardware, dimensions and pinout |
| [SDK download page](https://roboparty.feishu.cn/docx/RIKJdBaQYoDGRfx4yDwcmBcpnwf) | revision 9 | Original package names and versions |
| [ROS example downloads](https://roboparty.feishu.cn/docx/ZP7ldU3L9owd4BxRPXEcpclrnog) | revision 4 | Original ROS resources |
| [ROS example instructions](https://roboparty.feishu.cn/docx/F1fydcBSKo2H4jxjtyDccqUwnnc) | revision 1 | Identification of the original Humble/EtherCAT route |
| [Model downloads](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d) | revision 7 | DH116/DH116S archive information |
| [Host application downloads](https://roboparty.feishu.cn/docx/VnbPdcs9toG7a1xe9l2cwVujnOe) | revision 6 | Package names and versions |
| [Gesture application downloads](https://roboparty.feishu.cn/docx/UDyrdMlzyoJ1YaxHlb8cwkFenXg) | revision 67 | Windows/Linux names and versions |
| [CAN-FD protocol](https://roboparty.feishu.cn/docx/NofXd7ZqKovElLxfgr8cWMegnxg) | revision 14, relevant sections | Travel units and communication |
| [SDK](https://github.com/Roboparty/roboparty_dexhand/tree/046108e7ba800763a096ca1c99b04a8414797105) | `046108e` | Support scope, API, installation and acceptance |
| [ROS package](https://github.com/Roboparty/roboparty_dexhand_ros/tree/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227) | `bfc325f` | Integration status and limitations |
| [Company homepage](https://github.com/Roboparty/rptest_repo/tree/f1ca45288a61985d2372cbe38d767869d818eb8d) | `f1ca452` | Product animation `assets/readme/rp1-hand.gif` |

Original Feishu pages and the company homepage repository may require permission. Local hardware illustrations and text do not depend on remote image tokens for rendering.

## Asset mapping

| Local file | Source |
| --- | --- |
| `assets/dimensions.png` | User-manual image `IJRgbzn0PotT42x6EyHcbG7Qn9e`, original content preserved |
| `assets/pinout.png` | User-manual image `NPObb1VGQo1CpZxsHzScTKBwnVe`, original content preserved |
| `assets/rp-hand.gif` | Company homepage `assets/readme/rp1-hand.gif`, original content preserved |

Checksums for all three assets are in [SHA256SUMS.txt](../assets/SHA256SUMS.txt). Run `sha256sum -c assets/SHA256SUMS.txt` from the repository root to verify integrity.

## Resource archive

The upstream [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05) was recorded as a private resource prerelease containing 12 Feishu originals totaling 1,409,480,165 bytes. On 2026-10-06, the then-unpublished left/right CAD files were losslessly wrapped in XZ, reducing total downloads to 975,103,906 bytes. The tag identifies the snapshot date, not a replacement for each attachment's version. Original sizes were checked individually. The manifest records compressed and original CAD sizes/hashes, with decompressed byte identity verified.

The upstream record states that Git's [manifest.json](../resources/resources-2026.10.05/manifest.json), [SHA256SUMS.txt](../resources/resources-2026.10.05/SHA256SUMS.txt) and [validation.json](../resources/resources-2026.10.05/validation.json) matched same-named release attachments. Large files are outside Git history. SDK v0.5.0 binaries remain maintained in the SDK repository.

Create a new snapshot for future updates rather than overwriting published attachments. Update source revision, file size, hash and inspection records together. Decompression and format checks do not establish software safety, target-system compatibility or actual hardware acceptance.

## Update procedure

1. Verify product content in Feishu and record document revisions and attachment versions.
2. Put confirmed text in the corresponding Markdown, images in `assets/`, and large attachments in versioned releases.
3. Check local links, images and example syntax. For device behavior, record the actual software/hardware combination and acceptance results.
4. Review changes through a PR, then update downloads and entry-point documentation. Maintain SDK API changes in the SDK repository.

Do not treat a Feishu document token as a public download URL. Do not store access credentials here. Download availability follows actual publication status.

## Next steps

- Confirm public-release scope and repository visibility; complete applicable documentation/asset licenses.
- Verify mapping among six active axes, left/right hands, DH116/DH116S and models.
- Establish a released image/SDK/ROS combination and resolve upstream installation and homing differences.
- Maintain future snapshots and update manifests/checksums after confirming version applicability.
- Maintain the English guides and update compatibility from actual test records.

No physical hardware motion tests were performed for this documentation edition.

## Fork translation record

This fork translates the repository Markdown from upstream commit `e43fd90970019b093d41c131d3839d375a74f2be` and adds experimental plans. Translation date: 2026-10-18. The source inventory JSON and checksums are retained byte-for-byte; [English metadata translations](resource-metadata-english.md) are separate. See [translation status](translation-status.md) for scope and limitations.
