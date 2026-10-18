# SDK Integration

[Home](../README.md) · [Quick start](quickstart.md) · [Downloads](downloads.md)

## Choose an SDK

| Route | Use case | Entry point |
| --- | --- | --- |
| RoboParty-maintained wrapper | Linux CAN-FD, six active RP Hand axes, C++/Python applications and robot integration | [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand) |
| Original vendor SDK | Vendor Windows/Linux packages and their EtherCAT, CAN-FD and RS485 examples; consult the original instructions for supported combinations | [Original resources](downloads.md) |

This project recommends the first route by default. The older `roboparty_hand` interfaces `hand_py` and `connect_by_config()` are different from the current `dexhand_py`; do not mix their tutorials.

## Wrapper structure

Python applications access the public `HandDriver` through `dexhand_py`; C++ applications use `HandDriver` directly. The private `LHandProDriver` connects the vendor SDK adapter, SocketCAN transport, callbacks and lifecycle management. The vendor `libLHandProLib.so` remains an underlying dependency.

| Name | Meaning |
| --- | --- |
| `roboparty_dexhand` | SDK source project |
| `roboparty-dexhand` | Debian package |
| `dexhand_py` | Python extension module |
| `HandDriver` | Public C++/Python driver interface |
| `roboparty-dexhand-config` | Feedback-parameter configuration tool |
| `roboparty-base` | Base environment package providing `/opt/roboparty/setup.bash` |

## API and boundaries

- New programs use product name `RP_Hand`, interface `canfd` and `HandModel.RP_HAND_6DOF`.
- The factory does not communicate with the device. `init_hand()` establishes the session, with explicit choices for enabling and homing.
- After successful creation, call `deinit_hand()` using `try/finally` or corresponding C++ exception handling.
- Only one active hand instance is allowed per process. Use two processes for two hands.
- Read axis IDs are `1..6`. In control methods supporting broadcast, `0` means all axes, not the first finger.
- `get_now_*()` reads cached data. `check_health()` does not replace timestamp-based feedback freshness checks.
- The current public API has no tactile readout. Retained legacy enum values do not imply that RP Hand supports 16 active axes.

The SDK labels position in encoder counts, speed in counts/second, angle in degrees and current in mA. The raw CAN-FD protocol separately describes a total-travel coefficient with a default of 10000. Before connecting to a model using radians, verify the conversion and range for each axis on the actual device; do not assume a universal linear conversion.

## Authoritative documentation

This integration guide is based on SDK commit `046108e7ba800763a096ca1c99b04a8414797105`. Full documentation lives in the SDK repository:

- [Python/C++ API and examples](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/api.md)
- [CAN-FD and feedback configuration](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/hardware-setup.md)
- [Source build and Debian packaging](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/build.md)
- [Hardware acceptance](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/VALIDATION.md)
- [Released packages](https://github.com/Roboparty/roboparty_dexhand/releases)
- [Vendor binary versions and licensing](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/thirdparty/README.md)

Source-documentation baselines and releases are distinct version identifiers. Record package version, target operating system and Python ABI when installing. The date of the main branch is not package compatibility information.
