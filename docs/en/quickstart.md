# Single-hand CAN-FD quick start

[Home](../../README.md) · [中文](../quickstart.md) · [Hardware](hardware.md) · [Compatibility](compatibility.md)

Use the current [rphand source SDK](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) on a Linux target. Complete the offline build before connecting a device; then bring up one hand before adding ROS or the second hand.

## 1. Dependencies and build

Requirements: Linux, Git, CMake ≥ 3.20 and a C++17 compiler. Python bindings additionally require Python ≥ 3.9, matching development headers and pybind11. On Ubuntu:

```bash
sudo apt update
sudo apt install build-essential cmake git python3-dev pybind11-dev can-utils
git clone https://github.com/Roboparty/roboparty_dexhand.git
cd roboparty_dexhand
git checkout eb923acf61a02febabc9db90ad4d5eed84ffbc39
bash build.sh cpp
RPHAND_PYTHON=/usr/bin/python3 bash build.sh python
RPHAND_PYTHON=/usr/bin/python3 source setup_python.sh
/usr/bin/python3 -c 'from rphand import Hand; print(Hand)'
```

Build and run with the same Python interpreter. If CMake cannot locate pybind11, install its CMake package for that environment or set `pybind11_DIR` to the output of `python3 -m pybind11 --cmakedir` when using a pip installation. Do not copy old native extensions into the new package.


The core C++ project declares a 3.16 minimum, but this guide uses Python Development.Module (available from CMake 3.18) and `ctest --test-dir` (3.20). Use CMake 3.20 or later for the complete workflow. See the [CMake 3.20 release notes](https://cmake.org/cmake/help/v3.20/release/3.20.html#ctest).

## 2. Offline checks

Run from the SDK root:

```bash
cmake -S . -B build/check -DRPHAND_BUILD_SMOKE=ON -DRPHAND_BUILD_DEMO=ON
cmake --build build/check --parallel 2
ctest --test-dir build/check --output-on-failure
```

The upstream tests use simulated responses or unavailable interface names. Passing them does not validate physical motion.

## 3. Wiring and interface

Connect power, ground, CANH and CANL with power off, using the [connector drawing](hardware.md). Confirm the hand's actual node ID, supply and bus topology. The examples use `can0`, node `1`.

```bash
ip -details -statistics link show can0
```

The interface must be UP and CAN-FD. The reference bus rates are 1 Mbit/s arbitration and 5 Mbit/s data. Only configure an unconfigured interface after stopping all controllers sharing it:

```bash
sudo ip link set can0 down
sudo ip link set can0 type can bitrate 1000000 dbitrate 5000000 fd on
sudo ip link set can0 up
```

The SDK does not create interfaces or set bus rates. Current `connect()` configures and checks the six-axis 20 ms feedback cycle; the legacy feedback CLI is not part of this route.

## 4. Connect and read state

Stop other programs controlling the same device. Load `setup_python.sh` from the SDK root in each new shell, then run:

```python
from rphand import Hand

hand = Hand()
try:
    if not hand.connect("can0", 1):
        raise RuntimeError("Hand connection failed")
    state = hand.get_state()
    print("feedback_valid:", state.feedback_valid)
    print("positions:", state.positions)
    print("fault_codes:", state.fault_codes)
finally:
    hand.disconnect()
```

This example does not request enable or homing. However, connect writes communication configuration and may disable the hand and recover a latched software stop. It is not a read-only probe.

## 5. Motion and integration

Confirm mechanical clearance and stopping arrangements before using the upstream [C++ / Python wave examples](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39/examples). They enable, home and repeatedly send targets, including full-travel thumb targets. Do not use them as a first loaded test in a constrained workspace.

The normal sequence is `connect → disable → configure → enable → home → position control → stop / disable → disconnect`. Check every result, valid feedback and the actual device response. Disconnect only releases local resources; it does not stop or disable the hand.

Continue with [ROS 2](ros2.md) for dual-hand integration. Record the hardware/firmware, hand side, interface/ID, SDK commit, target OS/Python and observed test results. This documentation update did not perform device-motion acceptance.
