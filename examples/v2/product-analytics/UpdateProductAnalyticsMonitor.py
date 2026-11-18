"""
Update a Product Analytics monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_monitor_options import ProductAnalyticsMonitorOptions
from datadog_api_client.v2.model.product_analytics_monitor_request_type import ProductAnalyticsMonitorRequestType
from datadog_api_client.v2.model.product_analytics_monitor_thresholds import ProductAnalyticsMonitorThresholds
from datadog_api_client.v2.model.product_analytics_monitor_update_attributes import (
    ProductAnalyticsMonitorUpdateAttributes,
)
from datadog_api_client.v2.model.product_analytics_monitor_update_data import ProductAnalyticsMonitorUpdateData
from datadog_api_client.v2.model.product_analytics_monitor_update_request import ProductAnalyticsMonitorUpdateRequest

body = ProductAnalyticsMonitorUpdateRequest(
    data=ProductAnalyticsMonitorUpdateData(
        attributes=ProductAnalyticsMonitorUpdateAttributes(
            name="Funnel conversion drop",
            options=ProductAnalyticsMonitorOptions(
                thresholds=ProductAnalyticsMonitorThresholds(
                    critical=1.0,
                    warning=1.5,
                ),
            ),
        ),
        type=ProductAnalyticsMonitorRequestType.PA_MONITOR_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_product_analytics_monitor"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.update_product_analytics_monitor(monitor_id="12345", body=body)

    print(response)
