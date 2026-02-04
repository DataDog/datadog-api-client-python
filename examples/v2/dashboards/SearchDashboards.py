"""
Search dashboards returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

configuration = Configuration()
configuration.unstable_operations["search_dashboards"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.search_dashboards()

    print(response)
