"""
Create a Product Analytics launch returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_launch_create_data import ProductAnalyticsLaunchCreateData
from datadog_api_client.v2.model.product_analytics_launch_create_request import ProductAnalyticsLaunchCreateRequest
from datadog_api_client.v2.model.product_analytics_launch_event import ProductAnalyticsLaunchEvent
from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
from datadog_api_client.v2.model.product_analytics_launch_request_attributes import (
    ProductAnalyticsLaunchRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_launch_steps_request import ProductAnalyticsLaunchStepsRequest
from datadog_api_client.v2.model.product_analytics_launch_tracking_plan_request import (
    ProductAnalyticsLaunchTrackingPlanRequest,
)
from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType

body = ProductAnalyticsLaunchCreateRequest(
    data=ProductAnalyticsLaunchCreateData(
        attributes=ProductAnalyticsLaunchRequestAttributes(
            context="Let users apply promo codes at checkout.",
            description="Promo codes at checkout.",
            kpis=[
                ProductAnalyticsLaunchKPI(
                    id="7c1e6a52-3a8f-4d4e-9a55-2f1d1c8b6a10",
                    title="Checkout conversion rate",
                ),
            ],
            name="checkout_promo_codes",
            phase=ProductAnalyticsLaunchPhase.PLAN,
            steps=ProductAnalyticsLaunchStepsRequest(
                tracking_plan=ProductAnalyticsLaunchTrackingPlanRequest(
                    events=[
                        ProductAnalyticsLaunchEvent(
                            kpis=[
                                "7c1e6a52-3a8f-4d4e-9a55-2f1d1c8b6a10",
                            ],
                            name="promo_code_applied",
                            trigger="The user applies a valid promo code.",
                            views=[
                                "/checkout",
                            ],
                        ),
                    ],
                ),
            ),
        ),
        type=ProductAnalyticsLaunchType.LIFTOFF,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_product_analytics_launch"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.create_product_analytics_launch(body=body)

    print(response)
