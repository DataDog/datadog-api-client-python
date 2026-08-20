"""
Compute journey funnel analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
from datadog_api_client.v2.model.product_analytics_event_query_data_source import ProductAnalyticsEventQueryDataSource
from datadog_api_client.v2.model.product_analytics_event_search import ProductAnalyticsEventSearch
from datadog_api_client.v2.model.product_analytics_graph_query_group_by import ProductAnalyticsGraphQueryGroupBy
from datadog_api_client.v2.model.product_analytics_graph_query_group_by_source import (
    ProductAnalyticsGraphQueryGroupBySource,
)
from datadog_api_client.v2.model.product_analytics_group_by_sort import ProductAnalyticsGroupBySort
from datadog_api_client.v2.model.product_analytics_join_keys import ProductAnalyticsJoinKeys
from datadog_api_client.v2.model.product_analytics_journey_audience_account_query import (
    ProductAnalyticsJourneyAudienceAccountQuery,
)
from datadog_api_client.v2.model.product_analytics_journey_audience_filters import (
    ProductAnalyticsJourneyAudienceFilters,
)
from datadog_api_client.v2.model.product_analytics_journey_audience_segment_query import (
    ProductAnalyticsJourneyAudienceSegmentQuery,
)
from datadog_api_client.v2.model.product_analytics_journey_audience_user_query import (
    ProductAnalyticsJourneyAudienceUserQuery,
)
from datadog_api_client.v2.model.product_analytics_journey_funnel_compute import ProductAnalyticsJourneyFunnelCompute
from datadog_api_client.v2.model.product_analytics_journey_funnel_query import ProductAnalyticsJourneyFunnelQuery
from datadog_api_client.v2.model.product_analytics_journey_funnel_request import ProductAnalyticsJourneyFunnelRequest
from datadog_api_client.v2.model.product_analytics_journey_funnel_request_attributes import (
    ProductAnalyticsJourneyFunnelRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_journey_funnel_request_data import (
    ProductAnalyticsJourneyFunnelRequestData,
)
from datadog_api_client.v2.model.product_analytics_journey_node_target import ProductAnalyticsJourneyNodeTarget
from datadog_api_client.v2.model.product_analytics_journey_node_target_type import ProductAnalyticsJourneyNodeTargetType
from datadog_api_client.v2.model.product_analytics_journey_request_type import ProductAnalyticsJourneyRequestType
from datadog_api_client.v2.model.product_analytics_journey_search import ProductAnalyticsJourneySearch
from datadog_api_client.v2.model.product_analytics_journey_search_filters import ProductAnalyticsJourneySearchFilters
from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter import (
    ProductAnalyticsJourneySearchGraphFilter,
)
from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter_name import (
    ProductAnalyticsJourneySearchGraphFilterName,
)
from datadog_api_client.v2.model.product_analytics_journey_search_graph_filter_operator import (
    ProductAnalyticsJourneySearchGraphFilterOperator,
)
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder

body = ProductAnalyticsJourneyFunnelRequest(
    data=ProductAnalyticsJourneyFunnelRequestData(
        attributes=ProductAnalyticsJourneyFunnelRequestAttributes(
            exclude_anonymous_traffic=False,
            _from=1756425600000,
            query=ProductAnalyticsJourneyFunnelQuery(
                compute=ProductAnalyticsJourneyFunnelCompute(),
                group_by=[
                    ProductAnalyticsGraphQueryGroupBy(
                        facet="@geo.country",
                        should_exclude_missing=False,
                        sort=ProductAnalyticsGroupBySort(
                            aggregation="count",
                            order=QuerySortOrder.DESC,
                        ),
                        source=ProductAnalyticsGraphQueryGroupBySource.USERS,
                        target=ProductAnalyticsJourneyNodeTarget(
                            type=ProductAnalyticsJourneyNodeTargetType.NODE,
                            value="A",
                        ),
                        value_filters=[],
                    ),
                ],
                search=ProductAnalyticsJourneySearch(
                    expression="A -> B",
                    filters=ProductAnalyticsJourneySearchFilters(
                        audience_filters=ProductAnalyticsJourneyAudienceFilters(
                            accounts=[
                                ProductAnalyticsJourneyAudienceAccountQuery(
                                    name="enterprise_accounts",
                                ),
                            ],
                            formula="power_users AND NOT trial_segment",
                            segments=[
                                ProductAnalyticsJourneyAudienceSegmentQuery(
                                    name="trial_segment",
                                    segment_id="00000000-0000-0000-0000-000000000000",
                                ),
                            ],
                            users=[
                                ProductAnalyticsJourneyAudienceUserQuery(
                                    name="power_users",
                                ),
                            ],
                        ),
                        graph_filters=[
                            ProductAnalyticsJourneySearchGraphFilter(
                                name=ProductAnalyticsJourneySearchGraphFilterName.TIME_TO_CONVERT,
                                operator=ProductAnalyticsJourneySearchGraphFilterOperator.LESS_THAN_OR_EQUAL,
                                target=ProductAnalyticsJourneyNodeTarget(
                                    type=ProductAnalyticsJourneyNodeTargetType.NODE,
                                    value="A",
                                ),
                                value=60000,
                            ),
                        ],
                    ),
                    join_keys=ProductAnalyticsJoinKeys(
                        primary="@session.id",
                        secondary=[],
                    ),
                    node_objects=dict(
                        A=ProductAnalyticsEventQuery(
                            data_source=ProductAnalyticsEventQueryDataSource.PRODUCT_ANALYTICS,
                            search=ProductAnalyticsEventSearch(
                                query="@type:view @view.name:Login",
                            ),
                        ),
                        B=ProductAnalyticsEventQuery(
                            data_source=ProductAnalyticsEventQueryDataSource.PRODUCT_ANALYTICS,
                            search=ProductAnalyticsEventSearch(
                                query="@type:action @action.target.name:Submit",
                            ),
                        ),
                    ),
                ),
            ),
            to=1756857600000,
        ),
        type=ProductAnalyticsJourneyRequestType.JOURNEY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_product_analytics_journey_funnel"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_journey_funnel(body=body)

    print(response)
