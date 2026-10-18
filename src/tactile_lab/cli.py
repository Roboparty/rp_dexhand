"""Run experiments and save reproducible artifacts."""
import argparse
from pathlib import Path
from .evaluation.artifacts import write_json
from .evaluation.provenance import provenance
from .reporting import markdown_report

def main(argv=None):
    parser = argparse.ArgumentParser(description="Synthetic tactile research; no hardware commands")
    commands = parser.add_subparsers(dest="command", required=True)
    benchmark = commands.add_parser("benchmark")
    benchmark.add_argument("--experiment", choices=("pathways","receivers","combined","all"), default="all")
    benchmark.add_argument("--seed", type=int, default=42)
    benchmark.add_argument("--output", type=Path, default=Path("runs/latest"))
    replay = commands.add_parser("replay")
    replay.add_argument("input", type=Path)
    replay.add_argument("output", type=Path)
    replay.add_argument("--mode", choices=("raw","fixed","adaptive"), default="fixed")
    replay.add_argument("--unit", required=True)
    replay.add_argument("--source", choices=("synthetic","measured"), required=True)
    args=parser.parse_args(argv)
    if args.command == "replay":
        from .replay import replay_csv
        result=replay_csv(args.input,args.output,args.mode,args.unit,args.source)
        print(result)
        return 0
    if args.seed < 0:
        parser.error("seed must be nonnegative")
    from .pathways import run_benchmark as pathways
    from .receivers import run_benchmark as receivers
    from .combined import run_benchmark as combined
    jobs={"pathways":pathways,"receivers":receivers,"combined":combined}
    names=list(jobs) if args.experiment == "all" else [args.experiment]
    args.output.mkdir(parents=True,exist_ok=True)
    for name in names:
        result=jobs[name](args.seed)
        write_json(args.output/f"{name}.json",result)
        (args.output/f"{name}.md").write_text(markdown_report(result),encoding="utf-8")
        print(f"{name}: {args.output/name}")
    write_json(args.output/"provenance.json",provenance())
    return 0
