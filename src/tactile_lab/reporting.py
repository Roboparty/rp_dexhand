"""Human-readable reports retain failure cases and synthetic scope."""
def _fmt(value):
    return "unavailable" if value is None else f"{value:.4f}" if isinstance(value, float) else str(value)

def markdown_report(result):
    lines = [f"# {result['experiment'].replace('_', ' ').title()} Results", "",
             f"Evidence: **{result['evidence']}**", "", f"Configuration hash: `{result['config_sha256']}`", ""]
    if result["experiment"] == "pathway_graph":
        lines += ["| Model | Strength | Mean error (mm) | P95 error (mm) | Failures |",
                  "| --- | --- | --- | --- | --- |"]
        for name, model in result["models"].items():
            s = model["summary"]
            lines.append(f"| {name} | {_fmt(model['strength'])} | {_fmt(s['mean_error_mm'])} | {_fmt(s['p95_error_mm'])} | {s['failures']} |")
        p = result["paired_pathway_minus_spatial"]
        lines += ["", f"Pathway minus spatial error: {_fmt(p['mean_delta_mm'])} mm; paired bootstrap 95% interval: {p['bootstrap_95pct_interval_mm']}.",
                  f"Decision: **{result['decision']}**. Negative deltas favor pathways.",
                  "", "The fixed-strength ablation and condition-level results remain in the JSON artifact."]
    else:
        lines += ["| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |",
                  "| --- | --- | --- | --- | --- |"]
        for name, model in result["models"].items():
            s=model["summary"]
            lines.append(f"| {name} | {_fmt(model['threshold'])} | {_fmt(s['recall'])} | {_fmt(s['false_alarms_per_minute'])} | {_fmt(s['median_detected_latency_ms'])} |")
        lines += ["", "Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee."]
        if "recall_effects" in result:
            lines += ["", "## Descriptive factorial effects", ""]
            lines += [f"- {key}: {_fmt(value)}" for key,value in result["recall_effects"].items()]
    lines += ["", "## Limitations", ""]
    lines += ["- "+item for item in result["limitations"]]
    lines += ["", "## Reproduction", "", "Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded."]
    return "\n".join(lines)+"\n"
