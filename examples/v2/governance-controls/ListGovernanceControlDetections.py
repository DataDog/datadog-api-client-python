"""
List governance control detections returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_controls_api import GovernanceControlsApi

configuration = Configuration()
configuration.unstable_operations["list_governance_control_detections"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceControlsApi(api_client)
    response = api_instance.list_governance_control_detections(
        detection_type="detection_type",
    )

    print(response)
