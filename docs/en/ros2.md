# ROS 2 Jazzy integration

[Home](../../README.md) · [中文](../ros2.md) · [SDK](sdk.md) · [Compatibility](compatibility.md)

Use `ros2/rphand_ros` from the [same SDK baseline](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39). This C++ node includes dual-hand launch, target commands, reset and state feedback. The separate legacy Humble repository is not the current recommended path.

## Build and launch

Prepare [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html) and complete the [CAN interface checks](quickstart.md). From the SDK root:

```bash
source /opt/ros/jazzy/setup.bash
sudo apt install python3-colcon-common-extensions python3-rosdep
# Initialize rosdep as described in the ROS installation guide on first use.
rosdep update
rosdep install --from-paths ros2 --ignore-src -r -y --rosdistro jazzy
bash build.sh ros
source install/ros/local_setup.bash
ros2 launch rphand_ros dual_hand.launch.py command_rate_hz:=50
```

Set the command rate explicitly: launch otherwise defaults to 200 Hz, overriding YAML's 50 Hz. Left/right defaults are `can0` / `can3`, both node IDs 1. Add `right:=false` for left-hand-only operation; interfaces and IDs use `left_interface`, `right_interface`, `left_node_id`, `right_node_id`.

Launch waits for reset; it does not connect, enable or home the device. Load ROS and `install/ros/local_setup.bash` in every new shell.

## Reset and command

Reset enables and physically homes the hand. Confirm clearance first:

```bash
ros2 service call /dexhand_left/reset std_srvs/srv/Trigger '{}'
ros2 topic echo /dexhand_left/state
```

`success=true` means accepted, not completed. Wait for `Reset complete; waiting for a new target` and check fresh, valid, enabled/homed, fault-free feedback. Reset is not stop.

After initialization:

```bash
ros2 run rphand_ros command.py --side left 0 0 1000 1000 1000 1000
```

Six values use the [SDK axis order](sdk.md) and absolute travel units 0..10000. Sending a zero target is neither stop nor home.

## Interfaces and recording

| Left-hand interface | Type | Content |
| --- | --- | --- |
| `/dexhand_left/cmd` | `std_msgs/msg/Int32MultiArray` | Six-axis position action |
| `/dexhand_left/state` | `rphand_ros/msg/DexHandState` | Feedback snapshot and validity |
| `/dexhand_left/reset` | `std_srvs/srv/Trigger` | Accept a session initialization/homing request |

Replace left with right for the other hand. State contains position, velocity, current, enable, homed, torque-reached and fault arrays. There is no `/joint_states` publisher; model integration needs calibrated travel-to-radian conversion.

With rosbag2 CLI and storage support installed, record published state/action topics:

```bash
ros2 bag record -o rp_hand_session   /dexhand_left/cmd /dexhand_left/state   /dexhand_right/cmd /dexhand_right/state
```

Cmd has no in-message timestamp; bag records receive time. State's `header.stamp` is ROS publication time, not hardware sampling time. The two feedback groups are asynchronous. Check message age as well as `feedback_valid`; this recording recipe does not establish synchronization with whole-body cameras.

## Runtime boundaries

ROS repeatedly sends the last target at the configured rate. It has no command-timeout stop, no stop service and no automatic stop on invalid feedback. State publication targets 50 Hz but shares a thread with SDK calls and can pause during initialization, homing or blocking operations. Stopping the command publisher does not clear the device target. Normal node exit attempts stop/disable/disconnect; faults and forced termination can prevent cleanup.

Full parameters, examples and offline lifecycle tests are in the [upstream ROS guide](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/ros2.md). This update reviewed code and interfaces; it did not validate physical Jazzy operation.
