"""
List governance resource limits returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_settings_api import GovernanceSettingsApi

configuration = Configuration()
configuration.unstable_operations["list_governance_resource_limits"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceSettingsApi(api_client)
    response = api_instance.list_governance_resource_limits()

    print(response)
