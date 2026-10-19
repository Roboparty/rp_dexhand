# Configuration and gesture applications

[Home](../../README.md) · [中文](../software.md) · [Downloads](downloads.md)

Companion applications support device setup and demonstrations. Use the current C++ / Python SDK or bundled ROS interface to develop robot applications. These are separately maintained software paths.

| Application | Resource version | Platform and purpose |
| --- | --- | --- |
| RP Hand configuration application | 1.4.0, 2026-08-25 | Windows; device setup and parameter configuration |
| RP Hand Gesture | 1.1.1 | Windows EXE / Linux amd64 DEB; visual gesture-recognition demonstration |
| Current rphand SDK | Source baseline eb923ac | Linux; C++ / Python / bundled Jazzy ROS development |

Original packages and the host application's changelog are in [downloads](downloads.md). Follow each package's documentation for firmware, transport, OS, camera and dependencies. Do not apply original Windows/other-transport/legacy SDK instructions to the current source SDK.

The applications were not installed or executed in this documentation update, and direct compatibility with the current rphand API is not asserted. The presence of a gesture demo does not mean the current ROS node implements visual hand retargeting: recognition/retargeting belongs to the operator-side application, while the node handles device commands and feedback.

For custom control follow [quick start](quickstart.md); for published hand state/action recording see [ROS](ros2.md).
