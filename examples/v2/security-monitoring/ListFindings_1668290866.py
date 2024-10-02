"""
List findings with detection_type query param returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.finding_detection_type import FindingDetectionType

configuration = Configuration()
configuration.unstable_operations["list_findings"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_findings(
        filter_detection_type=[
            FindingDetectionType.MISCONFIGURATION,
            FindingDetectionType.ATTACK_PATH,
        ],
    )

    print(response)
