"""
Compute a Sankey diagram returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_audience_account_subquery import (
    ProductAnalyticsAudienceAccountSubquery,
)
from datadog_api_client.v2.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
from datadog_api_client.v2.model.product_analytics_audience_segment_subquery import (
    ProductAnalyticsAudienceSegmentSubquery,
)
from datadog_api_client.v2.model.product_analytics_audience_user_subquery import ProductAnalyticsAudienceUserSubquery
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
from uuid import UUID

body = ProductAnalyticsSankeyRequest(
    data=ProductAnalyticsSankeyRequestData(
        attributes=ProductAnalyticsSankeyRequestAttributes(
            definition=ProductAnalyticsSankeyDefinition(
                entries_per_step=10,
                number_of_steps=3,
                source="@view.name",
                target="@view.name",
            ),
            search=ProductAnalyticsSankeySearch(
                audience_filters=ProductAnalyticsAudienceFilters(
                    accounts=[
                        ProductAnalyticsAudienceAccountSubquery(
                            name="",
                        ),
                    ],
                    formula="u",
                    segments=[
                        ProductAnalyticsAudienceSegmentSubquery(
                            name="",
                            segment_id=UUID("00000000-0000-0000-0000-000000000000"),
                        ),
                    ],
                    users=[
                        ProductAnalyticsAudienceUserSubquery(
                            name="u",
                            query="*",
                        ),
                    ],
                ),
                join_keys=ProductAnalyticsJoinKeys(
                    primary="@session.id",
                    secondary=[],
                ),
                query="@type:view",
            ),
            time=ProductAnalyticsSankeyTime(
                _from=1756425600000,
                to=1756857600000,
            ),
        ),
        type=ProductAnalyticsSankeyRequestType.SANKEY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_product_analytics_sankey"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_sankey(body=body)

    print(response)
