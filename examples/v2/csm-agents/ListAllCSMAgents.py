"""
Get all CSM Agents returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_agents_api import CSMAgentsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CSMAgentsApi(api_client)
    response = api_instance.list_all_csm_agents()

    print(response)
