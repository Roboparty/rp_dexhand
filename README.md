# RP Hand

![CAN-FD](https://img.shields.io/badge/Transport-CAN--FD-2563eb)
![C++17](https://img.shields.io/badge/C%2B%2B-17-64748b)
![Python](https://img.shields.io/badge/Python-3.9%2B-64748b)
![ROS 2](https://img.shields.io/badge/ROS_2-Jazzy-64748b)

[English](README.md) | [简体中文](README.zh-CN.md)

**A compact six-axis dexterous hand, with C++, Python and ROS 2 interfaces for robot integration.**

![RP Hand quick-change installation on RP1](assets/rp-hand.gif)

RP Hand is a five-finger dexterous hand for small and medium humanoid robots, with CAN-FD connectivity for robot control. This repository provides wiring guides, software setup and model resources. Control code is maintained in [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand).

**Maintainer:** RoboParty · **Support:** [GitHub Issues](https://github.com/Roboparty/rp_dexhand/issues) · **Platform:** [RP1](https://github.com/Roboparty/RP1)

## Features

- Five fingers, 11 mechanical degrees of freedom and 6 actively controlled axes.
- CAN-FD integration with RP1, including internal cable routing through the matching platform connection.
- Shared `rphand::Hand` / `rphand.Hand` control implementation for C++ and Python.
- Bundled `rphand_ros` nodes with command topics, reset services and state feedback.
- A Windows configuration application and Windows/Linux gesture-recognition demo packages.
- Left/right CAD, URDF and MJCF resources with versioned downloads and checksums.

The recommended path is **Linux + CAN-FD + the current source SDK**. Original attachments for other transports are archived separately. See [compatibility](docs/en/compatibility.md) for current and legacy APIs.

## Companion tools

| Tool | Development use | Guide |
| --- | --- | --- |
| Windows configuration application | Device setup and parameter configuration | [Applications](docs/en/software.md) |
| Gesture-recognition demo | Visual gesture demonstration; Windows / Linux packages | [Gesture application](docs/en/software.md) |
| C++ / Python / ROS 2 | Custom control, robot integration and feedback recording | [SDK](docs/en/sdk.md) · [ROS](docs/en/ros2.md) |
| CAD / URDF / MJCF | Mechanical integration and robot-model development | [Models](docs/en/models.md) |

## Product specifications

| Property | Product manual |
| --- | --- |
| Dimensions | 147.54 × 73.53 × 26.35 mm |
| Mass | 379 ± 10 g |
| Actuation | 6 active axes; 5 additional passive/coupled DoF |
| Transmission | Worm gear |
| Integration | CAN-FD; mechanical/electrical details in the hardware guide |

Confirm the supplied hardware revision before integration. [Dimensions, power and pinout →](docs/en/hardware.md)

## Documentation

| Guide | Contents |
| --- | --- |
| [Quick start](docs/en/quickstart.md) | Dependencies, source build, CAN interface and first connection |
| [C++ / Python SDK](docs/en/sdk.md) | API entry points, six-axis order, units and state validity |
| [ROS 2 integration](docs/en/ros2.md) | Jazzy setup, commands, feedback and data recording |
| [Hardware](docs/en/hardware.md) | Dimensions, power and CAN-FD pinout |
| [Models](docs/en/models.md) | Left/right CAD, URDF/MJCF and mapping status |
| [Downloads](docs/en/downloads.md) | Configuration application, gesture demo, SDK and original assets |
| [Compatibility](docs/en/compatibility.md) | Current SDK baseline and migration from legacy interfaces |
| [Troubleshooting](docs/en/troubleshooting.md) | Build, connection, motion and feedback checks |

## Getting started

This guide uses [SDK `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39). It requires Linux, CMake ≥ 3.20 and a C++17 compiler; Python bindings require Python ≥ 3.9, development headers and pybind11. The bundled ROS build targets Jazzy. See [compatibility](docs/en/compatibility.md) when selecting a version or upgrading an existing installation.

```bash
git clone https://github.com/Roboparty/roboparty_dexhand.git
cd roboparty_dexhand
git checkout eb923acf61a02febabc9db90ad4d5eed84ffbc39
bash build.sh cpp
RPHAND_PYTHON=/usr/bin/python3 bash build.sh python
RPHAND_PYTHON=/usr/bin/python3 source setup_python.sh
/usr/bin/python3 -c 'from rphand import Hand; print(Hand)'
```

These commands build and import the SDK without connecting to a hand. Continue with [the quick start](docs/en/quickstart.md) before connecting hardware. Current source builds use `rphand`, not the older `dexhand_py` package.

## Software architecture

```text
C++ application       Python application       ROS 2 Jazzy
rphand::Hand          rphand.Hand               rphand_ros
        \                  |                     /
         +---------- shared C++ SDK ------------+
                           |
                    Linux SocketCAN
                           |
                         CAN-FD
                           |
                         RP Hand
```

The SDK handles protocol encoding, feedback decoding and sessions. ROS adds periodic target transmission and state publication. [SDK details →](docs/en/sdk.md)

## Repository layout

| Path | Responsibility |
| --- | --- |
| `docs/` | Chinese product and integration guides |
| `docs/en/` | English getting-started and reference guides |
| `assets/` | Installation animation, dimensions and connector drawings |
| `resources/` | Versioned resource manifests, provenance and checksums |
| `tools/`, `tests/` | Offline documentation checks and validator tests |

## Contributing and licensing

See [CONTRIBUTING.md](CONTRIBUTING.md) for checks and issue routing. Source versions and validation boundaries are recorded in [maintenance](docs/maintenance.md).

See [LICENSES.md](LICENSES.md) for licensing information and [NOTICE.md](NOTICE.md) for source attribution.
