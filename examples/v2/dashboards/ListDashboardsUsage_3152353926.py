"""
Get usage stats for all dashboards returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

configuration = Configuration()
configuration.unstable_operations["list_dashboards_usage"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    items = api_instance.list_dashboards_usage_with_pagination(
        page_limit=500,
    )
    for item in items:
        print(item)
