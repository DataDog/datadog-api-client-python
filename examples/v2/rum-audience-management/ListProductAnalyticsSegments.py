"""
List segments returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_product_analytics_segments"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.list_product_analytics_segments()

    print(response)
