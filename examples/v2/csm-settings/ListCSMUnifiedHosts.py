"""
List unified hosts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_settings_api import CSMSettingsApi

configuration = Configuration()
configuration.unstable_operations["list_csm_unified_hosts"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMSettingsApi(api_client)
    response = api_instance.list_csm_unified_hosts()

    print(response)
