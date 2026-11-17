"""
Create a Product Analytics monitor returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_monitor_create_attributes import (
    ProductAnalyticsMonitorCreateAttributes,
)
from datadog_api_client.v2.model.product_analytics_monitor_create_data import ProductAnalyticsMonitorCreateData
from datadog_api_client.v2.model.product_analytics_monitor_create_request import ProductAnalyticsMonitorCreateRequest
from datadog_api_client.v2.model.product_analytics_monitor_options import ProductAnalyticsMonitorOptions
from datadog_api_client.v2.model.product_analytics_monitor_request_type import ProductAnalyticsMonitorRequestType
from datadog_api_client.v2.model.product_analytics_monitor_tags import ProductAnalyticsMonitorTags
from datadog_api_client.v2.model.product_analytics_monitor_thresholds import ProductAnalyticsMonitorThresholds
from datadog_api_client.v2.model.product_analytics_monitor_variable import ProductAnalyticsMonitorVariable

body = ProductAnalyticsMonitorCreateRequest(
    data=ProductAnalyticsMonitorCreateData(
        attributes=ProductAnalyticsMonitorCreateAttributes(
            message="Conversion from /a to /b dropped over the last hour\n\n@slack-my-alerts-channel",
            name="Funnel conversion drop",
            options=ProductAnalyticsMonitorOptions(
                thresholds=ProductAnalyticsMonitorThresholds(
                    critical=1.0,
                    warning=2.0,
                ),
                variables=[
                    ProductAnalyticsMonitorVariable(
                        [
                            ("data_source", "product_analytics_journey"),
                            ("name", "query"),
                            (
                                "search",
                                "{'expression': 'node_0->node_1', 'filters': {'graph_filters': [{'name': '__dd.time_to_convert', 'operator': '<=', 'value': 86400000}]}, 'join_keys': {'primary': '@usr.id'}, 'node_objects': {'node_0': {'data_source': 'product_analytics', 'search': {'query': '@type:view @view.name:/a'}}, 'node_1': {'data_source': 'product_analytics', 'search': {'query': '@type:view @view.name:/b'}}}}",
                            ),
                        ]
                    ),
                ],
            ),
            priority=3,
            query='formula("query").rollup("sum").last("1h") < 1',
            tags=ProductAnalyticsMonitorTags(
                chart_id="chart-1",
                query_type="funnel",
            ),
        ),
        type=ProductAnalyticsMonitorRequestType.PA_MONITOR_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_product_analytics_monitor"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.create_product_analytics_monitor(body=body)

    print(response)
