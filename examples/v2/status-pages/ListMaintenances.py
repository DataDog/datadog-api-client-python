"""
List maintenances returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.list_maintenances()

    print(response)
