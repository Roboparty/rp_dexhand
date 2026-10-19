# URDF, MJCF and CAD

[Home](../../README.md) · [中文](../models.md) · [Downloads](downloads.md)

The resource snapshot includes DH116 and DH116S left/right URDF/MJCF archives dated 2026-04-09, plus revision-A DH116S white-hand CAD in Parasolid X_T format. CAD is losslessly wrapped in XZ. Choose the exact supplied hand model and verify checksums before extraction.

## DH116S model structure

Each DH116S hand contains 17 links, 11 movable joints (6 independent and 5 mimic), plus 5 fixed joints. The archive includes the files referenced by its 34 URDF and 17 MJCF mesh entries.

Independent joint names are `finger11`, `finger12`, `finger21`, `finger31`, `finger41`, `finger51`. Joint-tree, mimic and resource-reference details are listed in the [model record](../../resources/model-inspection-2026.10.19.json).

URDF uses `package://DH116S-L000-A1/...` or the corresponding right-hand package. Keep package/mesh resolution available. MJCF uses relative mesh directories; preserve the archive's directory layout.

## Device mapping

The [SDK channel order](sdk.md) is source-defined. Physical left/right axis correspondence, zero/sign and travel-to-radian conversion still require calibration for the supplied firmware and model. Preserve the five mimic relationships rather than sending all 11 model joints as independent device commands.

Calibrate zero/sign and travel-to-radian conversion before driving real hardware. Some URDF effort/velocity fields are zero; configure output limits using the actual device parameters. Treat model angular limits and SDK travel targets 0..10000 separately. The current ROS node publishes custom device state rather than joint_states.

CAD is supplied in its original X_T format. After importing it into your design software, check wrist mounting dimensions and assembly clearance against the matching engineering drawing. [Download instructions →](downloads.md)
