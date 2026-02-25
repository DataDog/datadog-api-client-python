"""
Compute timeseries analytics returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_analytics_query import ProductAnalyticsAnalyticsQuery
from datadog_api_client.v2.model.product_analytics_analytics_request import ProductAnalyticsAnalyticsRequest
from datadog_api_client.v2.model.product_analytics_analytics_request_attributes import (
    ProductAnalyticsAnalyticsRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_analytics_request_data import ProductAnalyticsAnalyticsRequestData
from datadog_api_client.v2.model.product_analytics_analytics_request_type import ProductAnalyticsAnalyticsRequestType
from datadog_api_client.v2.model.product_analytics_compute import ProductAnalyticsCompute
from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
from datadog_api_client.v2.model.product_analytics_event_query_data_source import ProductAnalyticsEventQueryDataSource
from datadog_api_client.v2.model.product_analytics_event_search import ProductAnalyticsEventSearch

body = ProductAnalyticsAnalyticsRequest(
    data=ProductAnalyticsAnalyticsRequestData(
        attributes=ProductAnalyticsAnalyticsRequestAttributes(
            _from=1771232048460,
            query=ProductAnalyticsAnalyticsQuery(
                compute=ProductAnalyticsCompute(
                    aggregation="count",
                ),
                query=ProductAnalyticsEventQuery(
                    data_source=ProductAnalyticsEventQueryDataSource.PRODUCT_ANALYTICS,
                    search=ProductAnalyticsEventSearch(
                        query="@type:view",
                    ),
                ),
            ),
            to=1771836848262,
        ),
        type=ProductAnalyticsAnalyticsRequestType.FORMULA_ANALYTICS_EXTENDED_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_timeseries(body=body)

    print(response)
