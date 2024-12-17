"""
Get all CSM Serverless Agents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_agents_api import CSMAgentsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMAgentsApi(api_client)
    response = api_instance.list_all_csm_serverless_agents()

    print(response)
