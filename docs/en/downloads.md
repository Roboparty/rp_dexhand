# Downloads

[Home](../../README.md) · [中文](../downloads.md) · [Compatibility](compatibility.md)

## Current SDK

Build the [current source baseline](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) following [quick start](quickstart.md). It provides C++, Python and bundled Jazzy ROS interfaces.

## Applications and models

Download the configuration application, gesture demos, models, CAD and protocol workbook from [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05). Choose a version below and verify its SHA-256 after downloading.

Install each application using the instructions included in its package. For robot software development, use the current `rphand` source SDK above.

| Resource | Source version | Download size, MB |
| --- | --- | --- |
| [RP_Hand_Protocols_EtherCAT_CAN-FD_RS485.xlsx](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Protocols_EtherCAT_CAN-FD_RS485.xlsx) | document revision 13 | 0.37 |
| [DH116_URDF_MJCF_Files_2026_4_9.7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116_URDF_MJCF_Files_2026_4_9.7z) | 2026-04-09 | 7.22 |
| [DH116S_URDF_MJCF_Files_2026_4_9.7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S_URDF_MJCF_Files_2026_4_9.7z) | 2026-04-09 | 9.56 |
| [RP_Hand_Host_changelog.txt](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Host_changelog.txt) | document revision 6 | 0.07 |
| [RP_Hand-v1.4.0-2026-08-25.zip](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand-v1.4.0-2026-08-25.zip) | 1.4.0 / 2026-08-25 | 205.57 |
| [RP-Hand-Gesture-Setup-1.1.1.exe](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-Setup-1.1.1.exe) | 1.1.1 | 299.84 |
| [RP-Hand-Gesture-1.1.1-amd64.deb](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-1.1.1-amd64.deb) | 1.1.1 | 309.22 |
| [DH116S-L000-A1_RP_Left_White_A.x_t.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-L000-A1_RP_Left_White_A.x_t.xz) | A | 45.29 |
| [DH116S-R000-A1_RP_Right_White_A.x_t.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-R000-A1_RP_Right_White_A.x_t.xz) | A | 43.56 |

Sizes are decimal MB. The two CAD downloads are XZ archives; their expanded original sizes and hashes are stored separately in the manifest. The original vendor routes are separate from the maintained current CAN-FD SDK.

<details>
<summary>Legacy SDK packages and original examples</summary>

These downloads are for maintaining matching existing installations. Use the SDK at the top of this page for current CAN-FD development.

| Resource | Source version | Download size, MB |
| --- | --- | --- |
| [RP_Hand_SDK-API-Linux-20260727.tar.gz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Linux-20260727.tar.gz) | 2026-07-27 | 13.43 |
| [RP_Hand_SDK-API-Windows-20260727.7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Windows-20260727.7z) | 2026-07-27 | 7.63 |
| [hand_control_ws_rp_hand.zip](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/hand_control_ws_rp_hand.zip) | document revision 4; no package version asserted | 33.35 |

Older `dexhand_py` packages are available in the [v0.5.0 release](https://github.com/Roboparty/roboparty_dexhand/releases/tag/v0.5.0). See [compatibility](compatibility.md) for API differences.

</details>

## Integrity checks

Download the files and the release's SHA256SUMS.txt into one directory, then:

```bash
sha256sum -c SHA256SUMS.txt
```

For one file, compute its SHA-256 and compare the entire value with the [checksum list](../../resources/resources-2026.10.05/SHA256SUMS.txt). CAD example:

```bash
xz -dk DH116S-L000-A1_RP_Left_White_A.x_t.xz
sha256sum DH116S-L000-A1_RP_Left_White_A.x_t
```

Compare the expanded hash with `original_sha256` in [manifest.json](../../resources/resources-2026.10.05/manifest.json). Do not compare it with the compressed-file hash.

Resource versions and original filenames are listed in [manifest.json](../../resources/resources-2026.10.05/manifest.json). See [hardware](hardware.md) for wiring, [models](models.md) for model integration and [source records](../maintenance.md) for provenance.
