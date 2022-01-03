from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds


def test_default_coerce():
    thresholds = MonitorThresholds(critical=5)
    assert thresholds["critical"] == 5.0
