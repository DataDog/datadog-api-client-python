"""
Unlink a Product Analytics monitor from its chart returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_monitor_unlink_attributes import (
    ProductAnalyticsMonitorUnlinkAttributes,
)
from datadog_api_client.v2.model.product_analytics_monitor_unlink_data import ProductAnalyticsMonitorUnlinkData
from datadog_api_client.v2.model.product_analytics_monitor_unlink_request import ProductAnalyticsMonitorUnlinkRequest
from datadog_api_client.v2.model.product_analytics_monitor_unlink_request_type import (
    ProductAnalyticsMonitorUnlinkRequestType,
)

body = ProductAnalyticsMonitorUnlinkRequest(
    data=ProductAnalyticsMonitorUnlinkData(
        attributes=ProductAnalyticsMonitorUnlinkAttributes(
            chart_id="chart-1",
            dashboard_id="dash-1",
        ),
        type=ProductAnalyticsMonitorUnlinkRequestType.PA_MONITOR_UNLINK_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["remove_chart_from_product_analytics_monitor"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    api_instance.remove_chart_from_product_analytics_monitor(monitor_id="12345", body=body)
