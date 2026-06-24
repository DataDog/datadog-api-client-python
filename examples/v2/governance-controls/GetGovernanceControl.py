"""
Get a governance control returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_controls_api import GovernanceControlsApi

configuration = Configuration()
configuration.unstable_operations["get_governance_control"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceControlsApi(api_client)
    response = api_instance.get_governance_control(
        detection_type="detection_type",
    )

    print(response)
