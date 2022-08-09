"""
List all the RUM applications returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.get_rum_applications()

    print(response)
