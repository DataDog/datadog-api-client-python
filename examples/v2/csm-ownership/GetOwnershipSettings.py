"""
Get ownership settings for the org returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi

configuration = Configuration()
configuration.unstable_operations["get_ownership_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.get_ownership_settings()

    print(response)
