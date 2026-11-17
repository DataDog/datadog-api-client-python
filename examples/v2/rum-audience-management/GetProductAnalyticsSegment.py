"""
Get a segment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_product_analytics_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.get_product_analytics_segment(
        id="8a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d",
    )

    print(response)
