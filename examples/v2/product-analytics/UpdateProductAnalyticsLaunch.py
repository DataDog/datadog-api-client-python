"""
Update a Product Analytics launch returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_launch_patch_attributes import ProductAnalyticsLaunchPatchAttributes
from datadog_api_client.v2.model.product_analytics_launch_patch_data import ProductAnalyticsLaunchPatchData
from datadog_api_client.v2.model.product_analytics_launch_patch_request import ProductAnalyticsLaunchPatchRequest
from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType

body = ProductAnalyticsLaunchPatchRequest(
    data=ProductAnalyticsLaunchPatchData(
        attributes=ProductAnalyticsLaunchPatchAttributes(
            phase=ProductAnalyticsLaunchPhase.SETUP,
        ),
        id="5e3c7a1b-2d4f-4e6a-8b9c-0d1e2f3a4b5c",
        type=ProductAnalyticsLaunchType.LIFTOFF,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_product_analytics_launch"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.update_product_analytics_launch(id="5e3c7a1b-2d4f-4e6a-8b9c-0d1e2f3a4b5c", body=body)

    print(response)
