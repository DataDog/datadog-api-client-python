"""
List analytics events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_analytics_list_query import ProductAnalyticsAnalyticsListQuery
from datadog_api_client.v2.model.product_analytics_analytics_list_request import ProductAnalyticsAnalyticsListRequest
from datadog_api_client.v2.model.product_analytics_analytics_list_request_attributes import (
    ProductAnalyticsAnalyticsListRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_analytics_list_request_data import (
    ProductAnalyticsAnalyticsListRequestData,
)
from datadog_api_client.v2.model.product_analytics_analytics_list_request_type import (
    ProductAnalyticsAnalyticsListRequestType,
)
from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
from datadog_api_client.v2.model.product_analytics_event_query_data_source import ProductAnalyticsEventQueryDataSource
from datadog_api_client.v2.model.product_analytics_event_search import ProductAnalyticsEventSearch

body = ProductAnalyticsAnalyticsListRequest(
    data=ProductAnalyticsAnalyticsListRequestData(
        attributes=ProductAnalyticsAnalyticsListRequestAttributes(
            _from=1771232048460,
            query=ProductAnalyticsAnalyticsListQuery(
                columns=[
                    "@view.name",
                ],
                limit=100,
                query=ProductAnalyticsEventQuery(
                    data_source=ProductAnalyticsEventQueryDataSource.PRODUCT_ANALYTICS,
                    search=ProductAnalyticsEventSearch(
                        query="@type:view",
                    ),
                ),
            ),
            to=1771836848262,
        ),
        type=ProductAnalyticsAnalyticsListRequestType.FORMULA_ANALYTICS_EXTENDED_LIST_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_product_analytics_list"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_list(body=body)

    print(response)
