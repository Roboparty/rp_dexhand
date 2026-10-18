"""Evaluate all requested seeds and retain complete results."""
from pathlib import Path
from .pathways import run_benchmark as pathways
from .receivers import run_benchmark as receivers
from .combined import run_benchmark as combined
from .ablation import run_benchmark as ablation
from .evaluation.artifacts import write_json
from .evaluation.provenance import provenance
from .reporting import markdown_report

def run_sweep(seeds, output):
    if not seeds or len(set(seeds))!=len(seeds) or any(isinstance(s,bool) or not isinstance(s,int) or s<0 for s in seeds):
        raise ValueError("provide distinct nonnegative integer seeds")
    output=Path(output); rows=[]
    for seed in seeds:
        directory=output/f"seed-{seed}"; directory.mkdir(parents=True,exist_ok=True)
        for name,runner in (("pathways",pathways),("receivers",receivers),("combined",combined),("ablation",ablation)):
            result=runner(seed)
            write_json(directory/f"{name}.json",result)
            (directory/f"{name}.md").write_text(markdown_report(result),encoding="utf-8")
            for model,values in result["models"].items():
                rows.append({"seed":seed,"experiment":name,"model":model,**values["summary"]})
    summary={"evidence":"synthetic seed sensitivity; no hardware or population inference",
             "seeds":list(seeds),"rows":rows}
    write_json(output/"summary.json",summary)
    write_json(output/"provenance.json",provenance())
    lines=["# Seed Robustness Study","","All requested seeds are retained. These are generator repetitions, not physical replications.","",
           "| Seed | Experiment | Model | Mean localization error (mm) | Recall | False alarms/min |",
           "| --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        def fmt(key):
            v=row.get(key)
            return "—" if v is None else f"{v:.4f}"
        lines.append(f"| {row['seed']} | {row['experiment']} | {row['model']} | {fmt('mean_error_mm')} | {fmt('recall')} | {fmt('false_alarms_per_minute')} |")
    (output/"SUMMARY.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    return summary
