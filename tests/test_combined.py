from tactile_lab.combined import run_benchmark,multichannel_trials
from tactile_lab.evaluation.artifacts import canonical_json

def test_shared_data_dimensions():
    trials,arrays,p=multichannel_trials(1,1)
    assert len(trials)==len(arrays)==24
    assert all(a.shape==(800,16) for a in arrays)

def test_four_conditions_share_trial_identities():
    r=run_benchmark(1,1)
    identities=[[t["trial_id"] for t in m["trials"]] for m in r["models"].values()]
    assert len(identities)==4 and all(i==identities[0] for i in identities)
    assert "synthetic" in r["evidence"]
    canonical_json(r)
