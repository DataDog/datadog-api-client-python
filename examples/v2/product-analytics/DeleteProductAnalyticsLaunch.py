"""
Delete a Product Analytics launch returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_product_analytics_launch"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    api_instance.delete_product_analytics_launch(
        id="5e3c7a1b-2d4f-4e6a-8b9c-0d1e2f3a4b5c",
    )
