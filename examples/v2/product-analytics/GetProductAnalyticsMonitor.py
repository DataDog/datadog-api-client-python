"""
Get a Product Analytics monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi

configuration = Configuration()
configuration.unstable_operations["get_product_analytics_monitor"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.get_product_analytics_monitor(
        monitor_id="12345",
    )

    print(response)
