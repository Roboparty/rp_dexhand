from tactile_lab.reporting import markdown_report

def test_null_latency_report():
    result={"experiment":"adaptive_receiver","evidence":"synthetic","config_sha256":"abc","models":{"fixed":{"threshold":1,"summary":{"recall":0,"false_alarms_per_minute":0,"median_detected_latency_ms":None}}},"limitations":["No hardware test."]}
    report=markdown_report(result)
    assert "unavailable" in report and "synthetic" in report and "No hardware test." in report
