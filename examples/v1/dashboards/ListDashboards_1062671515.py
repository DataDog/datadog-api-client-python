"""
Get all dashboards returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    items = api_instance.list_dashboards_with_pagination(
        count=2,
    )
    for item in items:
        print(item)
