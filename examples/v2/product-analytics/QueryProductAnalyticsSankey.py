"""
Compute Sankey flow analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys
from datadog_api_client.v2.model.product_analytics_sankey_definition import ProductAnalyticsSankeyDefinition
from datadog_api_client.v2.model.product_analytics_sankey_request import ProductAnalyticsSankeyRequest
from datadog_api_client.v2.model.product_analytics_sankey_request_attributes import (
    ProductAnalyticsSankeyRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_sankey_request_data import ProductAnalyticsSankeyRequestData
from datadog_api_client.v2.model.product_analytics_sankey_request_type import ProductAnalyticsSankeyRequestType
from datadog_api_client.v2.model.product_analytics_sankey_search import ProductAnalyticsSankeySearch
from datadog_api_client.v2.model.product_analytics_sankey_time import ProductAnalyticsSankeyTime

body = ProductAnalyticsSankeyRequest(
    data=ProductAnalyticsSankeyRequestData(
        attributes=ProductAnalyticsSankeyRequestAttributes(
            data_source="product_analytics",
            definition=ProductAnalyticsSankeyDefinition(
                entries_per_step=5,
                number_of_steps=5,
                source="/logs",
                target="",
            ),
            search=ProductAnalyticsSankeySearch(
                join_keys=ProductAnalyticsJoinKeys(
                    primary="@session.id",
                ),
                query="@type:view",
            ),
            time=ProductAnalyticsSankeyTime(
                _from=1771232048460,
                to=1771836848262,
            ),
        ),
        type=ProductAnalyticsSankeyRequestType.SANKEY_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_sankey(body=body)

    print(response)
