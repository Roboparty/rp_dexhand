# URDF, MJCF and CAD

[Home](../README.md) · [Hardware dimensions](hardware.md) · [Downloads](downloads.md)

## Available resources

| Resource | Source version | Recorded status |
| --- | --- | --- |
| DH116 URDF/MJCF | `DH116_URDF_MJCF_Files_2026_4_9.7z` | Archived; 7z integrity check passed |
| DH116S URDF/MJCF | `DH116S_URDF_MJCF_Files_2026_4_9.7z` | Archived; 7z integrity check passed |
| Left-hand CAD | DH116S-L000-A1 structural component, RP left-hand DH116S-LW1-RP1 kit, white, revision A; exact original filename is in the manifest | XZ download: 45,285,532 bytes; restored: 260,959,468 bytes |
| Right-hand CAD | DH116S-R000-A1 structural component, RP right-hand DH116S-RW1-RP1 kit, white, revision A; exact original filename is in the manifest | XZ download: 43,559,368 bytes; restored: 262,261,691 bytes |

The upstream [resource release](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05) was recorded as private and requires appropriate GitHub access. See [Downloads](downloads.md) for retrieval and verification. The [original URDF/MJCF page](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d) and [CAD attachments in the product manual](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb) remain source records.

Both model archives include corresponding `L000-A1` and `R000-A1` directories, with `urdf/*.urdf`, `mjcf/*.xml` and meshes for each side. Full paths are in the [inspection report](../resources/resources-2026.10.05/validation.json). Only archive integrity and directory listings were checked; mesh references, simulation loading and physical joint mapping were not validated.

DH116 and DH116S filenames are not unconditionally interchangeable. The current RoboParty SDK's public model 0 maps internally to Dof6S, but this does not replace checking the delivered hardware and model version.

## Mapping requirements

Before connecting a model to hardware, verify each axis:

| Field | Record |
| --- | --- |
| SDK active axis | ID 1–6 |
| Physical meaning | Finger and lateral-swing or flexion/extension motion |
| Left/right hand | Model side, direction and mounting coordinate frame |
| Model joint | Actual URDF/MJCF joint name |
| Zero and positive direction | Relationship between SDK and model zero positions |
| Units and range | Conversion from device position/angle to model radians, plus per-axis limits |
| Passive/coupled joints | Coupling relationships or mimic definitions for the five additional DOF |

A verified mapping table has not been published. Do not guess joint order from names, assign six inputs directly to all 11 model joints, or assume a common travel coefficient means the same angular conversion for every axis.

## Future file organization

Large CAD and original model archives use versioned releases; Git stores only documentation, inventories and checksums. CAD uses lossless XZ compression and the restored original hashes were verified. Geometry was only inspected at the file-header level, not accepted in CAD software. Decide whether to store model text and meshes directly in Git after checking reference paths and applicable versions.

Continue to use [single-hand SDK acceptance](quickstart.md) as the runtime foundation. Model visualization is not a substitute for actual device feedback.
