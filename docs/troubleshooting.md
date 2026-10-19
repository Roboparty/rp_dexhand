# Troubleshooting

[Home](../README.md) · [Quick start](quickstart.md)

| Symptom | Checks |
| --- | --- |
| Missing `/opt/roboparty/setup.bash` | Check whether the image includes `roboparty-base`; source installations use the paths specified in the SDK build guide |
| `ModuleNotFoundError: dexhand_py` | Load the matching environment in the current shell, use the matching system Python and inspect the installation path |
| Failure to import a `.so` | Check CPU architecture, Python ABI and all dependencies; do not mix source-built and image-bundled extensions |
| Missing `can0` | Use `ip -brief link` to find the actual interface; check the adapter, wiring and Linux driver |
| Communication failure or feedback timeout | Check power, CAN-FD 1 Mbps/5 Mbps, node ID, feedback configuration and other controlling processes |
| Settings lost after power-off | Check that configuration used `--save`, then run `show` again after power cycling the hand |
| Homing failure | Inspect fresh position/status feedback and alarms; do not bypass homing and continue moving |
| Second hand cannot open in the same process | Vendor callback resources are process-wide; use one process per hand |
| Communication initializes but the hand does not move | `init_hand(False, False, 0.0)` does not enable motion; enabling and homing require a separate explicit procedure |
| Changing init parameters after initialization fails | Call `deinit_hand()`, then recreate/reinitialize; repeated init is not a state transition |
| ROS cannot find `configure_feedback` | The inspected ROS package does not provide it; use the SDK's `roboparty-dexhand-config` |
| ROS has no `/joint_states` | Publication is not implemented in the current CAN-FD ROS package; vendor EtherCAT examples do not apply |
| Feishu attachments cannot open | Original resources require access; check Downloads for a GitHub mirror. An access problem is not a driver fault |

## Collect diagnostics

These commands do not send motion commands:

```bash
uname -m
/usr/bin/python3 --version
dpkg-query -W roboparty-dexhand roboparty-base
ip -details -statistics link show can0
/usr/bin/python3 -c 'import dexhand_py; print(dexhand_py.__file__)'
```

Load the matching software environment before the final command. Replace `can0` with the target interface. Record hardware model/left or right hand, firmware, driver version, system image, node ID, steps performed and complete errors.

Getter readings are cached. A zero reading alone does not prove a device is offline; a nonempty reading alone does not prove feedback is updating. Check software faults, communication failures and mechanical motion outcomes separately.
