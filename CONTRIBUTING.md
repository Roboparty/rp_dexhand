# Contributing

[English home](README.md) · [中文首页](README.zh-CN.md)

## Where to contribute

| Topic | Repository |
| --- | --- |
| Product documentation, wiring, resources and examples on these pages | [rp_dexhand](https://github.com/Roboparty/rp_dexhand/issues) |
| Current SDK, Python bindings and bundled rphand_ros runtime | [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand/issues) |
| Existing legacy Humble nodes | [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros/issues) |

## Documentation changes

1. Record the source hardware/software version and link to the relevant file, commit or manual revision.
2. Update both README languages and the corresponding guides. Keep current and legacy API paths separate.
3. Distinguish source inspection, offline tests, simulator checks and real-device results. Do not infer device capability from a download filename.
4. Preserve existing resource manifests/checksums. Add a new dated record for new resources or verification results.
5. Run the local checks using Python 3.9 or later:

```bash
python3 -m unittest discover -s tests -v
python3 tools/check_docs.py
```

The checker validates local links/heading fragments, Python snippet syntax, product-asset checksums and consistency of resource filenames/hashes. It does not execute device examples, fetch external links or revalidate archived application binaries. GitHub Actions runs these same checks.

## Device issue reports

Include hardware/firmware, left/right hand, CAN interface and node ID, SDK commit, OS/architecture/Python/ROS, reproduction steps and logs. For feedback issues, include message age and `feedback_valid`; values alone do not prove freshness. Share measurements and timestamps with their units and clock source.

中文：本仓库接受产品与文档改进；SDK 及同仓库 ROS 运行时代码问题请在 SDK 仓库提交。修改参数或接口说明时同步更新中英文内容，保留来源和验证边界。请勿提交访问 token、个人信息、未经授权的附件或未声明来源的性能结论。

Licensing boundaries are documented in [LICENSES.md](LICENSES.md). Contributions do not grant additional rights to archived third-party material.
