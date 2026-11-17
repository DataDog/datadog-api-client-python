"""
List Product Analytics monitors returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi

configuration = Configuration()
configuration.unstable_operations["list_product_analytics_monitors"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.list_product_analytics_monitors()

    print(response)
