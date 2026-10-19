# Single-Hand CAN-FD Quick Start

[Home](../README.md) · [Wiring](hardware.md) · [Troubleshooting](troubleshooting.md)

This procedure uses the maintained `roboparty_dexhand` driver for the six active axes of RP Hand. Match example interface `can0` and node ID `1` to the actual hardware. Read the wiring guide first and stop other programs controlling the same hand.

## 1. Choose an installation method

| Environment | Entry point |
| --- | --- |
| RoboParty image with the driver installed | Proceed to the environment checks below |
| Package confirmed compatible with the operating system, Python and CPU architecture | Obtain it from [Downloads](downloads.md); `roboparty-base` is also required for the shared environment entry point |
| Development or another environment | Build from source using the [SDK build instructions](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/build.md) |

The current SDK documentation baseline is Ubuntu 24.04 with system Python 3.12. The Python extension must match the interpreter version and CPU architecture. Source builds do not provide a repository-root `setup.bash`; use the path configuration in the build guide. The driver can run without ROS.

## 2. Check the image's software environment

Run these commands in Bash on the controller. They do not connect to, enable or home the hand:

```bash
source /opt/roboparty/setup.bash
/usr/bin/python3 -c 'import dexhand_py; print(dexhand_py.__file__)'
/usr/bin/python3 -c 'from dexhand_py import HandModel; print(HandModel.RP_HAND_6DOF.value)'
roboparty-dexhand-config --help
dpkg-query -W roboparty-dexhand roboparty-base
```

The module should come from `/opt/roboparty/`, the model value should be `0`, and the configuration tool should be available. If the environment script is missing, check the installation first. Do not copy the SDK's `.so` alone into another Python environment.

## 3. Check the interface

```bash
ip -details -statistics link show can0
```

The target interface should be `UP`, have CAN-FD enabled and show `bitrate 1000000` and `dbitrate 5000000`. If unconfigured, follow the [SDK CAN-FD setup](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/hardware-setup.md). Reconfiguring an interface interrupts communication on it.

## 4. Configure and verify the feedback period

Perform this step for a new or replacement device, after a factory reset, or when the configuration is unknown. It changes parameters on the hand; do not run a hand-control program concurrently.

```bash
roboparty-dexhand-config feedback-period apply --interface can0 --node-id 1 --milliseconds 20 --save
```

Power-cycle the hand itself, then query:

```bash
roboparty-dexhand-config feedback-period show --interface can0 --node-id 1
```

All six axes should report raw value `200`. Even if `apply` returns `already-compliant`, complete the readback after power cycling. Normal `init_hand()` does not persist the feedback period.

20 ms means approximately 50 Hz for each of two feedback types, or about 100 frames/second/hand combined. It is not a 100 Hz sampling rate for a single state type, nor a promise of a 500 Hz whole-system control loop.

## 5. Initialize communication only

This example sends initialization configuration to the device, but does not request enabling or homing. Complete the power, interface and feedback setup first:

```python
from dexhand_py import HandDriver, HandModel

hand = HandDriver.create_hand(
    "RP_Hand", "canfd", "can0", HandModel.RP_HAND_6DOF, 1
)
try:
    if not hand.init_hand(False, False, 0.0):
        raise RuntimeError("Communication initialization failed")
    hand.check_health()
    print("total DOF, active DOF:", hand.get_dof())
finally:
    hand.deinit_hand()
```

Expected DOF is `(11, 6)`. This checks driver initialization only; it does not establish successful motion, homing or fresh feedback. Confirm the process has exited before proceeding to motion.

## 6. Enable, home and move one hand

This stage causes physical motion. Clear the motion envelope, prepare a hardware stopping method, and confirm target values and speed for the mechanism and load.

Use the SDK-maintained [complete Python/C++ examples](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/api.md). They cover enabling, homing, moving to a target, returning to zero and releasing resources. If initialization fails, stop and diagnose it; do not bypass homing with `set_move_no_home(1)`.

`home_wait_time=5.0` is a maximum wait in seconds; success returns earlier. A newly created instance needs fresh position and status feedback after homing to confirm the result. For recovery after only a process restart, with the hand still powered and its zero position trustworthy, follow the SDK documentation. Do not apply that assumption to a cold start.

## 7. Acceptance and two-hand expansion

Use the [SDK deployment and acceptance SOP](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/VALIDATION.md) to check actual motion, position feedback, alarms, frame rates and parameter persistence. Getters return cached data; a fixed wait does not prove that motion completed.

Record device model/left or right hand, firmware, operating system/Python, SDK version, CAN interface and node ID, then record the results. This is a consolidated procedure, not a claim that your device has passed physical testing.

Keep one OS process per hand. Read [ROS versions and current limitations](ros2.md) before using ROS.
