"""Sensitivity analysis, not a search for the best test-set configuration."""
from dataclasses import replace,asdict
import numpy as np
from .receivers import generate_dataset,CausalReceiver
from .receivers.training import fit_config,threshold_candidates,select_threshold
from .receivers.metrics import evaluate_trial,aggregate
from .evaluation import validate_splits,content_hash

def run_benchmark(seed=42,trials_per_scenario=4):
    data=generate_dataset(seed,trials_per_scenario)
    splits=validate_splits(data)
    base=fit_config([t for t in data if t.split=="train"])
    variants={"fixed":("fixed",base),"adaptive":("adaptive",base),
              "faster_noise_tracking":("adaptive",replace(base,noise_alpha=.03)),
              "looser_gate":("adaptive",replace(base,adaptation_gate=10.)),
              "slower_envelope":("adaptive",replace(base,envelope_alpha=.05))}
    models={}
    for name,(mode,cfg) in variants.items():
        scores=[CausalReceiver(mode,cfg).replay(t.samples) for t in data]
        train=np.concatenate([s for t,s in zip(data,scores) if t.split=="train"])
        candidates=threshold_candidates(train)
        validation=[(t,s) for t,s in zip(data,scores) if t.split=="validation"]
        threshold,tuning=select_threshold([t for t,s in validation],[s for t,s in validation],candidates)
        rows=[evaluate_trial(t,s,threshold) for t,s in zip(data,scores) if t.split=="test"]
        models[name]={"threshold":threshold,"receiver":asdict(cfg),"summary":aggregate(rows),
                      "validation_candidates":tuning,"trials":rows,
                      "by_scenario":{c:aggregate([r for r in rows if r["scenario"]==c]) for c in sorted({r["scenario"] for r in rows})}}
    config={"seed":seed,"trials_per_scenario_per_split":trials_per_scenario,
            "variants":{k:{"mode":m,"config":asdict(c)} for k,(m,c) in variants.items()},
            "threshold_resolution":64,"false_alarm_budget_per_minute":3.}
    return {"experiment":"receiver_ablation","evidence":"synthetic sensitivity analysis",
            "config":config,"config_sha256":content_hash(config),"splits":splits,"models":models,
            "limitations":["Variants are reported together; test results do not choose a new winner.",
                           "Each variant independently calibrates its threshold on the same validation trials.",
                           "These changes isolate parameter sensitivity, not biological mechanisms.",
                           "A false-alarm budget on validation is not guaranteed on test."]}
