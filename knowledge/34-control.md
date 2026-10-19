# Bounded grip proposals and hardware limits

The pure simulated policy proposes c_new = min(1,c + step) when slip is detected and all guards pass. Here c is a normalized abstract command in [0,1], not a motor count or force. Without slip it holds c.

Guards block changes when stop is requested, homing is unverified, sensor age exceeds the limit, or measured force reaches the configured maximum. A blocked proposal returns the current command and a reason.

Example: c = 0.995 and step = 0.01 yields 1.0. If the same sample is stale, the proposed value stays 0.995 with allowed = false.

**Why used:** it demonstrates how detector output can be separated from permission to change a command.

**Limits:** this is not a dynamic grasp simulator, emergency-stop implementation or verified hardware controller. It sends nothing to CAN-FD. Holding the last command is not necessarily the physically safest action; a real device needs an independently designed failure policy.

The driver documentation describes position commands. Position changes are not automatically force control, and motor current is not a calibrated force sensor.

**Code:** [propose_grip](../src/tactile_lab/control.py). **Hardware context:** [guide](../docs/hardware.md).
