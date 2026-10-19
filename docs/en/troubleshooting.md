# Troubleshooting

[Home](../../README.md) · [中文](../troubleshooting.md) · [Quick start](quickstart.md)

| Symptom | Check |
| --- | --- |
| Cannot import rphand | Source setup_python.sh in the SDK root; use the build's Python interpreter |
| Only dexhand_py is installed | This is a legacy package; use the compatibility guide before migrating |
| pybind11 not found | Install its target-environment CMake package or set pybind11_DIR |
| Native extension import error | Match Python ABI, architecture and dependencies; rebuild on the target |
| No CAN-FD interface | Check adapter/system driver and interface configuration |
| connect fails | Check power, wiring, 1/5 Mbit/s, node ID, feedback and competing controllers |
| ROS launch produces no motion | Current nodes wait for reset and do not connect automatically |
| reset accepted but targets ignored | Wait for reset completion and verify fresh enabled/homed, fault-free state |
| Old values remain after disconnect | Check feedback_valid and message age; cached values can remain |
| No joint_states | Current ROS publishes custom state; model conversion needs calibration |
| Zero target does not stop/home | It is a position target, not a stop or home operation |
| Motion continues after publisher exits | ROS repeats its cached target; follow node cleanup and check the physical result |

Collect architecture, OS/Python/ROS, SDK commit, hardware/firmware, side, interface/ID and full initialization/error logs. Report documentation issues here and current SDK/bundled ROS issues upstream. Do not share access tokens or unauthorized attachments.

Useful non-motion diagnostics after loading the matching environment:

```bash
uname -m
/usr/bin/python3 --version
git -C /path/to/roboparty_dexhand rev-parse HEAD
ip -details -statistics link show can0
/usr/bin/python3 -c 'import rphand; print(rphand.__file__)'
```
