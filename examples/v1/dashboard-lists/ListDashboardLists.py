"""
Get all dashboard lists returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.list_dashboard_lists()

    print(response)
