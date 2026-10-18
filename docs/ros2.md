# ROS 2 Integration and Compatibility

[Home](../README.md) · [Connect one hand first](quickstart.md) · [SDK](sdk.md)

Robot-side integration is maintained in [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros). It controls devices through `dexhand_py`, with a separate process for each hand.

## Version status

| Source | Documented state | Interpretation |
| --- | --- | --- |
| SDK documentation `046108e` | Ubuntu 24.04, Python 3.12, image-bundled driver; targets Jazzy downstream | A standalone SDK documentation baseline, not validation of the complete ROS combination |
| ROS package `bfc325f` | Validated environment listed as Ubuntu 22.04, Python 3.10, Humble; minimum driver version 0.4.2 | Requires a driver matching that Python ABI; do not reuse Python 3.12 paths directly |
| Original Feishu ROS example | Humble/EtherCAT, `lhandpro_service` and RViz examples | A separate vendor integration route, not the current CAN-FD ROS package |

Upstream installation instructions differ: the ROS README references `~/roboparty_dexhand/setup.bash`, but the current SDK build guide explicitly does not provide that file. For source installation, use the build instructions for the corresponding SDK version.

The downstream `configure_feedback` mentioned in the SDK README was not implemented in the inspected ROS package. Use `roboparty-dexhand-config` from the [quick start](quickstart.md), stopping ROS nodes and other control processes before configuring.

## Existing interfaces

| Interface | Type | Behavior |
| --- | --- | --- |
| `/dexhand_left/cmd` | `std_msgs/msg/Int32MultiArray` | Six position commands in `0..10000`, executed at the configured speed |
| `/dexhand_left/init` | `std_srvs/srv/Trigger` | Recreates and enables the instance without homing; only for recovery with a trustworthy zero position |
| `/dexhand_left/reset` | `std_srvs/srv/Trigger` | Recreates, enables and homes; causes motion |

Replace `left` with `right` for the right hand. Default interfaces are `can0` for the left and `can3` for the right; match them to the actual wiring. Full parameters are maintained in the [ROS README](https://github.com/Roboparty/roboparty_dexhand_ros/blob/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227/README.md).

## Current limitations

The current node calls `set_move_no_home(1)` when handling position commands, allowing motion without completed homing. This differs from the SDK's recommended homing requirement; see the [node implementation](https://github.com/Roboparty/roboparty_dexhand_ros/blob/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227/roboparty_dexhand_ros/dexhand_node.py#L277). Until cold-start and recovery behavior is corrected and verified, prefer controlled single-hand SDK acceptance. This guide does not present the ROS default motion path as an accepted quick start.

The current CAN-FD ROS package does not publish position, status, current, alarms or `/joint_states`. Do not transfer RViz feedback capabilities from the original EtherCAT example to this package. Timestamped feedback and verified [joint mapping](models.md) are prerequisites for future RViz and rosbag workflows.

## Integration acceptance records

Record image version, Ubuntu, Python, ROS distribution, SDK package/tag, ROS commit, hardware/firmware, left/right interfaces and node IDs. Verify communication initialization, cold-start homing, recovery with a trustworthy zero, abnormal exit, isolation between two processes and feedback behavior separately.

This is an integration-status guide. It does not assert that Jazzy or Humble can be freely combined with any driver release.
