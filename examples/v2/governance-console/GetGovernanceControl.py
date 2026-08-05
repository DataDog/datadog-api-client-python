"""
Get a control returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_console_api import GovernanceConsoleApi

configuration = Configuration()
configuration.unstable_operations["get_governance_control"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceConsoleApi(api_client)
    response = api_instance.get_governance_control(
        detection_type="detection_type",
    )

    print(response)
