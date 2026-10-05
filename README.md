# RP Hand

[English](README.md) | [简体中文](README.zh-CN.md)

![RP Hand quick-swap attachment on RP1](assets/rp-hand.gif)

RP Hand is a compact dexterous hand for small and medium humanoid robots, with **11 mechanical degrees of freedom and 6 actively controlled axes**. This repository provides product documentation and integration guides. The maintained Linux CAN-FD driver is [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand).

| Product specification | Value |
| --- | --- |
| Dimensions | 147.54 x 73.53 x 26.35 mm |
| Weight | 379 g +/- 10 g |
| Transmission | Worm gear |
| Active axes | 6, with 5 additional passive/coupled degrees of freedom |
| Tactile sensing | Optional; not exposed by the current RoboParty driver API |

Specifications are transcribed from the product manual. Confirm the hardware revision and options of the supplied unit before integration.

## Start Here

The detailed guides below are currently in Simplified Chinese.

| Task | Guide |
| --- | --- |
| Check dimensions, power and wiring | [Hardware](docs/hardware.md) |
| Bring up one hand over CAN-FD | [Quick start](docs/quickstart.md) |
| Choose and use the maintained C++/Python SDK | [SDK integration](docs/sdk.md) |
| Integrate ROS 2 | [ROS 2 guide and compatibility](docs/ros2.md) |
| Find models and understand joint mapping | [URDF, MJCF and CAD](docs/models.md) |
| Download a versioned software package | [Downloads and availability](docs/downloads.md) |
| Diagnose setup and communication issues | [Troubleshooting](docs/troubleshooting.md) |

## Software Scope

| Component | Role and current scope |
| --- | --- |
| [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand) | Maintained Linux CAN-FD C++ driver, `dexhand_py` bindings and feedback configuration CLI; amd64 and arm64 packages |
| [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros) | One process per hand, command topics and initialization/reset services; see the ROS guide for version differences and current limitations |
| Vendor SDK and applications | Separate packages and examples, including other operating systems and transports; see the download table for availability |

The current RoboParty SDK route supports Linux CAN-FD and six active axes. Product-level Windows, EtherCAT, RS485 and tactile capabilities do not imply support in this wrapper. Two hands require separate OS processes. Driver getters return cached feedback.

The SDK documentation targets an Ubuntu 24.04 / Python 3.12 image; the current ROS README documents Ubuntu 22.04 / Python 3.10 / Humble. A combined Jazzy deployment is not presented here as verified. Use the [compatibility guide](docs/ros2.md) before combining packages.

## Resources and Maintenance

Dimensions and connector drawings are available locally in this repository. Twelve original software, model, CAD and protocol attachments are archived in the private prerelease [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05), with source records, file sizes and SHA-256 checksums in [Downloads](docs/downloads.md). Repository access is required. This resource snapshot is not a new SDK release or a hardware-validation result; maintained RoboParty driver releases are linked directly.

Report product-documentation issues in [this repository](https://github.com/Roboparty/rp_dexhand/issues), driver issues in [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand/issues), and ROS integration issues in [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros/issues).

[Source records and update procedure](docs/maintenance.md) | [Third-party and asset notices](NOTICE.md)
