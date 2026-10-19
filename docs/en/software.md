# Configuration and gesture applications

[Home](../../README.md) · [中文](../software.md) · [Downloads](downloads.md)

RP Hand includes a configuration application and gesture-recognition demos for device setup and visual demonstrations. Use the C++ / Python SDK or ROS 2 interface to develop custom control applications.

| Application | Resource version | Platform and purpose |
| --- | --- | --- |
| RP Hand configuration application | 1.4.0, 2026-08-25 | Windows; device setup and parameter configuration |
| RP Hand Gesture | 1.1.1 | Windows EXE / Linux amd64 DEB; visual gesture-recognition demonstration |
| Current rphand SDK | Source baseline eb923ac | Linux; C++ / Python / bundled Jazzy ROS development |

Download the applications and changelog from [downloads](downloads.md). Follow the package instructions to configure firmware, transport, OS dependencies and camera access.

Recognition and retargeting run in the operator-side application; the robot SDK / ROS node receives targets and controls the hand. When integrating a custom gesture application, output targets using the documented [axis order and units](sdk.md).

For custom control follow [quick start](quickstart.md); for published hand state/action recording see [ROS](ros2.md).
