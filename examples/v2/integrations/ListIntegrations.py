"""
List Integrations returns "Successful Response." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integrations_api import IntegrationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IntegrationsApi(api_client)
    response = api_instance.list_integrations()

    print(response)
