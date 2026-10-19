# Compatibility and migration

[Home](../../README.md) · [中文](../compatibility.md) · [Quick start](quickstart.md)

For new integrations, build [SDK eb923ac](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) from source on the target machine. Bring up one hand through the standalone SDK before adding its bundled ROS package.

| Route | Interface / environment | Status |
| --- | --- | --- |
| Current source SDK | `rphand::Hand`, `rphand.Hand`; Linux, C++17, CMake ≥ 3.20, Python ≥ 3.9 | Recommended for new integrations |
| Bundled ROS | `rphand_ros`; Jazzy | Includes state publication; same SDK source tree |
| Legacy SDK `046108e` / v0.5.0 packages | `HandDriver`, `dexhand_py` | Maintain existing matching installations only |
| Vendor packages / EtherCAT examples | Separate original SDKs and applications | Archived [downloads](downloads.md), not current CAN-FD APIs |

Migration requires application changes. `Hand()` and `connect()` replace the old factory/init API; connect manages feedback configuration. Current limits use thousandths of rated current, not mA. The new source SDK uses independent sessions rather than the legacy process-wide vendor callback. Multiple controllers must still not own the same interface/node.

Do not replace old extensions in place or mix old/new environment scripts. The old v0.5.0 `.deb` does not install the current `rphand` API. Record source commit and target Python ABI separately from package versions.

[CI](https://github.com/Roboparty/rp_dexhand/actions/runs/39203726788) checks the SDK's C++ / Python build, installation, offline tests and external CMake consumer on Ubuntu 24.04 x86-64.

Complete target-device checks for ARM64, ROS 2 and physical hand operation. Record OS/architecture, firmware, Python and motion conditions with the deployment configuration.

For an existing SDK installation, the reference source is [046108e](https://github.com/Roboparty/roboparty_dexhand/tree/046108e7ba800763a096ca1c99b04a8414797105). Use `ros2/rphand_ros` in the current SDK for ROS integration.
