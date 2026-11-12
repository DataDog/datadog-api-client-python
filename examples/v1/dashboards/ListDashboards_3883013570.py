"""
Get all dashboards with version "2027-01-01" returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1_20270101.api.dashboards_api import DashboardsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False,
    )

    print(response)
