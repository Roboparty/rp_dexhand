# C++ / Python SDK

[Home](../../README.md) · [中文](../sdk.md) · [Quick start](quickstart.md) · [ROS](ros2.md)

Baseline: [SDK eb923ac](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39). The C++ `rphand::Hand` and Python `rphand.Hand` share the same source-built protocol and device implementation. The old `HandDriver` / `dexhand_py` wrapper is a separate [legacy route](compatibility.md).

## Integration

| Entry point | Purpose |
| --- | --- |
| `<rphand/hand.hpp>` / `rphand::Hand` | C++ session, controls and state snapshots |
| `from rphand import Hand` | Python bindings |
| `rphand_ros` | Bundled Jazzy ROS integration |
| `bash build.sh cpp / python / ros` | Outputs in `install/cpp`, `install/python`, `install/ros` |

After installing the C++ component, external projects can use:

```cmake
find_package(rphand CONFIG REQUIRED)
add_executable(hand_app main.cpp)
target_link_libraries(hand_app PRIVATE rphand::rphand)
```

Set `CMAKE_PREFIX_PATH` to the SDK's `install/cpp`. The [upstream API](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/api.md) documents complete signatures and examples.

## Axis order and units

| Array index | Axis ID | Channel |
| --- | --- | --- |
| 0 | 1 | Thumb abduction |
| 1 | 2 | Thumb flexion |
| 2 | 3 | Index finger |
| 3 | 4 | Middle finger |
| 4 | 5 | Ring finger |
| 5 | 6 | Little finger |

This is the source-defined SDK order, not a calibrated device-to-URDF mapping.

| Quantity | Meaning |
| --- | --- |
| Position target | Absolute travel units, 0..10000; not degrees or radians |
| Speed | Travel units/second; ROS accepts 1..20000 |
| Current limit | Thousandths of rated current, 0..3000; not mA |
| Feedback current | Protocol-decoded value; not a force/torque measurement |
| Single-axis ID | 1..6; broadcast ID 0 is not accepted by the current public single-axis API |

## Control and feedback

Use `connect → disable → configure → enable → home → position control → stop / disable → disconnect`. Connect writes communication settings and may recover a latched stop. Position methods send a target once and do not wait for arrival, interpolate or periodically resend it. Applications must gate commands on initialization and health conditions.

`get_state()` immediately returns a cached snapshot with six-element `positions`, `velocities`, `currents`, `enabled`, `homed`, `torque_reached`, `fault_codes`, plus `feedback_valid`. Validity requires a healthy connection and both feedback groups younger than 100 ms. The groups are asynchronous and old array values can remain after invalidation. `is_connected()` alone is not a freshness check.

For Python cleanup, attempt and check both `stop()` and `disable()` before `disconnect()`, even if stop fails. C++ additionally offers `prepare_disconnect()` with one stop and one disable attempt. Disconnect and destruction release local resources without sending a stop.

The current API does not expose tactile sensing. See [architecture](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/architecture.md) for threads, cancellation and retry behavior, and [ROS](ros2.md) for state publication and recording.
