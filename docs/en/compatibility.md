# Compatibility and migration

[Home](../../README.md) · [中文](../compatibility.md) · [Quick start](quickstart.md)

Reviewed on 2026-10-19. For new integrations, build [SDK eb923ac](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) from source on the target machine. Bring up one hand through the standalone SDK before adding its bundled ROS package.

| Route | Interface / environment | Status |
| --- | --- | --- |
| Current source SDK | `rphand::Hand`, `rphand.Hand`; Linux, C++17, CMake ≥ 3.20, Python ≥ 3.9 | Recommended documentation baseline |
| Bundled ROS | `rphand_ros`; Jazzy | Includes state publication; same SDK source tree |
| Legacy SDK `046108e` / v0.5.0 packages | `HandDriver`, `dexhand_py` | Maintain existing matching installations only |
| Legacy ROS `bfc325f` | `roboparty_dexhand_ros`; Humble/Python 3.10 documentation | Commands and lifecycle services; legacy SDK dependency |
| Vendor packages / EtherCAT examples | Separate original SDKs and applications | Archived [downloads](downloads.md), not current CAN-FD APIs |

Migration requires application changes. `Hand()` and `connect()` replace the old factory/init API; connect manages feedback configuration. Current limits use thousandths of rated current, not mA. The new source SDK uses independent sessions rather than the legacy process-wide vendor callback. Multiple controllers must still not own the same interface/node.

Do not replace old extensions in place or mix old/new environment scripts. The old v0.5.0 `.deb` does not install the current `rphand` API. Record source commit and target Python ABI separately from package versions.

Source requirements are not a tested-hardware matrix. Current documents were checked against public headers, bindings, messages and build scripts. The pinned SDK's C++ / Python build, installation, offline tests and external CMake consumer were checked on GitHub-hosted Ubuntu 24.04 x86-64; see the [CI record](https://github.com/Roboparty/rp_dexhand/actions/runs/39203726788).

This check does not cover ARM64, ROS 2 builds/runtime, a real CAN bus or device motion. Verify the actual OS/architecture, firmware, Python and motion conditions during deployment.

Historical evidence: [SDK 046108e](https://github.com/Roboparty/roboparty_dexhand/tree/046108e7ba800763a096ca1c99b04a8414797105), [legacy ROS bfc325f](https://github.com/Roboparty/roboparty_dexhand_ros/tree/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227).
