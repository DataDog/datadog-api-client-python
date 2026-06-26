"""
Get governance notification settings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_settings_api import GovernanceSettingsApi

configuration = Configuration()
configuration.unstable_operations["get_governance_notification_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceSettingsApi(api_client)
    response = api_instance.get_governance_notification_settings()

    print(response)
