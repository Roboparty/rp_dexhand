# Downloads and Availability

[Home](../README.md) · [SDK selection](sdk.md) · [Models](models.md)

Resource snapshot: 2026-10-05. The upstream record describes 12 Feishu resources archived in [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05). Originals total 1,409,480,165 bytes; after lossless CAD compression, the 12 downloads total 975,103,906 bytes (about 975.10 MB). This is a resource prerelease, not a new SDK or a hardware acceptance result.

The snapshot recorded the upstream repository and release as private. This fork is public, but that does not establish current availability of the upstream attachments. Missing authentication or permissions may produce a 404. Original Feishu links require the appropriate Feishu access. Software and models retain their original packages; some download filenames use ASCII. CAD is wrapped in lossless XZ, with decompressed SHA-256 checked against the original Feishu files. Release attachments are not included in this Git checkout or copied into this fork.

## RoboParty-maintained driver

| Resource | Version/architecture | Download |
| --- | --- | --- |
| Linux Debian package | v0.5.0 / amd64 | [roboparty-dexhand_0.5.0-1_amd64.deb](https://github.com/Roboparty/roboparty_dexhand/releases/download/v0.5.0/roboparty-dexhand_0.5.0-1_amd64.deb) |
| Linux Debian package | v0.5.0 / arm64 | [roboparty-dexhand_0.5.0-1_arm64.deb](https://github.com/Roboparty/roboparty_dexhand/releases/download/v0.5.0/roboparty-dexhand_0.5.0-1_arm64.deb) |
| SDK source and other releases | As specified by the selected tag | [Source](https://github.com/Roboparty/roboparty_dexhand) · [Releases](https://github.com/Roboparty/roboparty_dexhand/releases) |
| ROS adapter source | See [ROS compatibility](ros2.md) | [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros) |

The upstream inventory confirmed these deb assets existed. They were not installed, executed or checksummed in that review; no cross-system/Python ABI compatibility is asserted. Confirm the target environment and obtain matching `roboparty-base` before installing. Users of a matching image generally do not need to reinstall.

## Vendor software and applications

| Resource | Version / size (decimal MB) | Release download |
| --- | --- | --- |
| Windows host application | 1.4.0 / 2026-08-25 / 205.57 MB | [ZIP](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand-v1.4.0-2026-08-25.zip) |
| Original host changelog | Source document revision 6 / 0.07 MB | [TXT](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Host_changelog.txt) |
| Windows gesture application | 1.1.1 / 299.84 MB | [EXE](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-Setup-1.1.1.exe) |
| Linux amd64 gesture application | 1.1.1 / 309.22 MB | [DEB](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-1.1.1-amd64.deb) |
| Vendor Linux SDK | 2026-07-27 / 13.43 MB | [tar.gz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Linux-20260727.tar.gz) |
| Vendor Windows SDK | 2026-07-27 / 7.63 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Windows-20260727.7z) |
| Vendor ROS example | Humble/EtherCAT; source document revision 4 / 33.35 MB | [ZIP](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/hand_control_ws_rp_hand.zip) |

Original sources: [host application](https://roboparty.feishu.cn/docx/VnbPdcs9toG7a1xe9l2cwVujnOe), [gesture application](https://roboparty.feishu.cn/docx/UDyrdMlzyoJ1YaxHlb8cwkFenXg), [vendor SDK](https://roboparty.feishu.cn/docx/RIKJdBaQYoDGRfx4yDwcmBcpnwf), [ROS example](https://roboparty.feishu.cn/docx/ZP7ldU3L9owd4BxRPXEcpclrnog). The original Linux SDK archive contains `aarch64`, `i386` and `x86_64` directories; their presence does not establish testing on a target system.

The vendor SDK/ROS examples and RoboParty CAN-FD wrapper are different software routes. Do not arbitrarily overwrite installed driver files with vendor `.so` files, or assume that capabilities of original examples exist in the current ROS package.

## Models and protocols

| Resource | Version / size (decimal MB) | Release download |
| --- | --- | --- |
| DH116 URDF/MJCF, both hands | 2026-04-09 / 7.22 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116_URDF_MJCF_Files_2026_4_9.7z) |
| DH116S URDF/MJCF, both hands | 2026-04-09 / 9.56 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S_URDF_MJCF_Files_2026_4_9.7z) |
| White DH116S left-hand CAD | L000-A1 / A / 45.29 MB (260.96 MB decompressed) | [X_T.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-L000-A1_RP_Left_White_A.x_t.xz) |
| White DH116S right-hand CAD | R000-A1 / A / 43.56 MB (262.26 MB decompressed) | [X_T.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-R000-A1_RP_Right_White_A.x_t.xz) |
| EtherCAT/CAN-FD/RS485 protocol workbook | Source manual revision 13 / 0.37 MB | [XLSX](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Protocols_EtherCAT_CAN-FD_RS485.xlsx) |

Original sources: [model download page](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d), [product manual attachments](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb). The [online CAN-FD protocol](https://roboparty.feishu.cn/docx/NofXd7ZqKovElLxfgr8cWMegnxg) is document revision 14; document revision alone does not establish how its protocol version compares with the attached workbook.

Dimension and pinout drawings are stored in the [hardware guide](hardware.md) and can be viewed without Feishu sign-in.

## Inventory and integrity checks

- [Complete manifest](../resources/resources-2026.10.05/manifest.json): original names, versions, model/platform, source documents and revisions, exact byte counts and SHA-256.
- [SHA256SUMS.txt](../resources/resources-2026.10.05/SHA256SUMS.txt): full checksums for 12 downloads (compressed archives for CAD); upstream recorded a matching release copy.
- [Inspection record](../resources/resources-2026.10.05/validation.json): per-file results and validation boundaries.
- [English metadata glossary](resource-metadata-english.md): translations of original filenames and workbook sheet identifiers retained verbatim in the records.

After downloading all 12 attachments and `SHA256SUMS.txt` to one directory, run there:

```bash
sha256sum -c SHA256SUMS.txt
```

For one attachment, such as a model package, run in its directory:

```bash
sha256sum DH116S_URDF_MJCF_Files_2026_4_9.7z
```

Compare the complete hash with the corresponding checksum record. Checksums establish byte identity, not source identity, signatures or software safety.

For CAD, verify the compressed hash before decompression. For example, preserve the archive while restoring the left-hand file on Linux:

```bash
xz -dk DH116S-L000-A1_RP_Left_White_A.x_t.xz
sha256sum DH116S-L000-A1_RP_Left_White_A.x_t
```

Compare the decompressed hash with `original_sha256` in the manifest; `original_size_bytes` records the original size. The right-hand procedure is equivalent. Windows users can use an XZ-capable extractor.

The upstream snapshot records ZIP/7z/gzip integrity checks, XZ restoration hashes, and Debian metadata/content listing checks. EXE and X_T inspection covered file type and headers only: no installers were executed, CAD geometry loaded, simulations run or real hardware driven. These are historical upstream checks, not newly performed by this translation. Public redistribution remains subject to the [third-party notice](../NOTICE.md).
