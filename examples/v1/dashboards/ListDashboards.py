"""
Get all dashboards returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

with ApiClient(Configuration()) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(filter_shared=False)

    print(response)
