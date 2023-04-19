"""
Get a finding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_finding"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_finding(
        finding_id="AgAAAYd59gjghzF52gAAAAAAAAAYAAAAAEFZZDU5Z2pnQUFCRTRvV1lFeEo4SlFBQQAAACQAAAAAMDE4NzdhMDEtMDRiYS00NTZlLWFmMzMtNTIxNmNkNjVlNDMz",
    )

    print(response)
