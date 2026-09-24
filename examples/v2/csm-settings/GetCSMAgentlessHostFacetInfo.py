"""
Get agentless host facet info returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_settings_api import CSMSettingsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_csm_agentless_host_facet_info"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMSettingsApi(api_client)
    response = api_instance.get_csm_agentless_host_facet_info(
        facet="cloud_provider",
    )

    print(response)
