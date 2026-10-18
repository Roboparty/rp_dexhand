from tactile_lab.ablation import run_benchmark

def test_variants_share_data_and_report_parameters():
    r=run_benchmark(3,1)
    assert len(r["models"])==5
    identities=[tuple(t["trial_id"] for t in m["trials"]) for m in r["models"].values()]
    assert all(x==identities[0] for x in identities)
    assert r["models"]["faster_noise_tracking"]["receiver"]["noise_alpha"]==.03
