"""
Count untagged findings by ownership confidence returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_ownership_untagged_findings"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.get_ownership_untagged_findings()

    print(response)
