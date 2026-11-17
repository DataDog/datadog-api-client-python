"""
Get monthly usage by resource supports non-host resources
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.monthly_resources_view import MonthlyResourcesView

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_monthly_resources(
        filter_billing_dimension="indexed_points",
        filter_month="2026-04",
        filter_view=MonthlyResourcesView.ALL,
        page_limit=1,
    )

    print(response)
