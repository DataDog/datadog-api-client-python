"""
Import threat intelligence feed returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.threat_intel_indicator_type import ThreatIntelIndicatorType

configuration = Configuration()
configuration.unstable_operations["import_threat_intel"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.import_threat_intel(
        ti_vendor="ti_vendor",
        ti_indicator=ThreatIntelIndicatorType.IP_ADDRESS,
    )
