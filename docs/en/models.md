# URDF, MJCF and CAD

[Home](../../README.md) · [中文](../models.md) · [Downloads](downloads.md)

The resource snapshot includes DH116 and DH116S left/right URDF/MJCF archives dated 2026-04-09, plus revision-A DH116S white-hand CAD in Parasolid X_T format. CAD is losslessly wrapped in XZ. Choose the exact supplied hand model and verify checksums before extraction.

## DH116S static inspection

On 2026-10-19, the DH116S archive hash was checked against the original manifest. Each hand contains 17 links, 11 movable joints (6 independent and 5 mimic), plus 5 fixed joints. Its 34 URDF mesh references and 17 MJCF mesh references resolve within the archive. Joint-tree and mimic-source references were also checked.

Independent joint names are `finger11`, `finger12`, `finger21`, `finger31`, `finger41`, `finger51`. See the [inspection record](../../resources/model-inspection-2026.10.19.json) for exact details. DH116 was not reinspected in this update.

URDF uses `package://DH116S-L000-A1/...` or the corresponding right-hand package. Keep package/mesh resolution available. MJCF uses relative mesh directories; preserve the archive's directory layout.

## Device mapping

The [SDK channel order](sdk.md) is source-defined. Physical left/right axis correspondence, zero/sign and travel-to-radian conversion still require calibration for the supplied firmware and model. Preserve the five mimic relationships rather than sending all 11 model joints as independent device commands.

XML/reference checks do not validate simulator loading or dynamics. Some URDF effort/velocity fields are zero and must not be treated as device capability ratings. Model angular limits are not automatically equivalent to manual ranges or SDK travel targets 0..10000. The current ROS node publishes custom device state rather than joint_states.

CAD geometry was not opened in a CAD application. The original archives, inertia, limits and linkage parameters remain unchanged. [Download instructions →](downloads.md)
