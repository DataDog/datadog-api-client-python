"""
List the entities behind a retention cell returns "OK" response
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
from datadog_api_client.v2.model.product_analytics_calendar_interval import ProductAnalyticsCalendarInterval
from datadog_api_client.v2.model.product_analytics_calendar_interval_type import ProductAnalyticsCalendarIntervalType
from datadog_api_client.v2.model.product_analytics_event_query import ProductAnalyticsEventQuery
from datadog_api_client.v2.model.product_analytics_event_query_data_source import ProductAnalyticsEventQueryDataSource
from datadog_api_client.v2.model.product_analytics_event_search import ProductAnalyticsEventSearch
from datadog_api_client.v2.model.product_analytics_retention_calendar_time_interval import (
    ProductAnalyticsRetentionCalendarTimeInterval,
)
from datadog_api_client.v2.model.product_analytics_retention_calendar_time_interval_type import (
    ProductAnalyticsRetentionCalendarTimeIntervalType,
)
from datadog_api_client.v2.model.product_analytics_retention_cell_scope import ProductAnalyticsRetentionCellScope
from datadog_api_client.v2.model.product_analytics_retention_cell_scope_type import (
    ProductAnalyticsRetentionCellScopeType,
)
from datadog_api_client.v2.model.product_analytics_retention_cohort_criteria import (
    ProductAnalyticsRetentionCohortCriteria,
)
from datadog_api_client.v2.model.product_analytics_retention_entity import ProductAnalyticsRetentionEntity
from datadog_api_client.v2.model.product_analytics_retention_filters import ProductAnalyticsRetentionFilters
from datadog_api_client.v2.model.product_analytics_retention_index_target import ProductAnalyticsRetentionIndexTarget
from datadog_api_client.v2.model.product_analytics_retention_index_target_type import (
    ProductAnalyticsRetentionIndexTargetType,
)
from datadog_api_client.v2.model.product_analytics_retention_list_column import ProductAnalyticsRetentionListColumn
from datadog_api_client.v2.model.product_analytics_retention_list_column_field import (
    ProductAnalyticsRetentionListColumnField,
)
from datadog_api_client.v2.model.product_analytics_retention_list_query import ProductAnalyticsRetentionListQuery
from datadog_api_client.v2.model.product_analytics_retention_list_request import ProductAnalyticsRetentionListRequest
from datadog_api_client.v2.model.product_analytics_retention_list_request_attributes import (
    ProductAnalyticsRetentionListRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_retention_list_request_data import (
    ProductAnalyticsRetentionListRequestData,
)
from datadog_api_client.v2.model.product_analytics_retention_list_request_type import (
    ProductAnalyticsRetentionListRequestType,
)
from datadog_api_client.v2.model.product_analytics_retention_return_condition import (
    ProductAnalyticsRetentionReturnCondition,
)
from datadog_api_client.v2.model.product_analytics_retention_return_criteria import (
    ProductAnalyticsRetentionReturnCriteria,
)
from datadog_api_client.v2.model.product_analytics_retention_search import ProductAnalyticsRetentionSearch
from uuid import UUID

body = ProductAnalyticsRetentionListRequest(
    data=ProductAnalyticsRetentionListRequestData(
        attributes=ProductAnalyticsRetentionListRequestAttributes(
            _from=1756425600000,
            query=ProductAnalyticsRetentionListQuery(
                columns=[
                    ProductAnalyticsRetentionListColumn(
                        field=ProductAnalyticsRetentionListColumnField(
                            path="@usr.email",
                        ),
                    ),
                ],
                computation_scope=ProductAnalyticsRetentionCellScope(
                    cohort_target=ProductAnalyticsRetentionIndexTarget(
                        type=ProductAnalyticsRetentionIndexTargetType.INDEX,
                        value=0,
                    ),
                    return_period_target=ProductAnalyticsRetentionIndexTarget(
                        type=ProductAnalyticsRetentionIndexTargetType.INDEX,
                        value=0,
                    ),
                    type=ProductAnalyticsRetentionCellScopeType.CELL,
                ),
                limit=100,
                search=ProductAnalyticsRetentionSearch(
                    cohort_criteria=ProductAnalyticsRetentionCohortCriteria(
                        base_query=ProductAnalyticsEventQuery(
                            data_source=ProductAnalyticsEventQueryDataSource.PRODUCT_ANALYTICS,
                            search=ProductAnalyticsEventSearch(
                                query="@type:view",
                            ),
                        ),
                        time_interval=ProductAnalyticsRetentionCalendarTimeInterval(
                            type=ProductAnalyticsRetentionCalendarTimeIntervalType.CALENDAR,
                            value=ProductAnalyticsCalendarInterval(
                                alignment="monday",
                                quantity=1,
                                timezone="UTC",
                                type=ProductAnalyticsCalendarIntervalType.WEEK,
                            ),
                        ),
                    ),
                    filters=ProductAnalyticsRetentionFilters(
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
                    ),
                    retention_entity=ProductAnalyticsRetentionEntity.USER_ID,
                    return_condition=ProductAnalyticsRetentionReturnCondition.CONVERSION_ON_OR_AFTER,
                    return_criteria=ProductAnalyticsRetentionReturnCriteria(
                        base_query=ProductAnalyticsEventQuery(
                            data_source=ProductAnalyticsEventQueryDataSource.PRODUCT_ANALYTICS,
                            search=ProductAnalyticsEventSearch(
                                query="@type:view",
                            ),
                        ),
                        time_interval=ProductAnalyticsRetentionCalendarTimeInterval(
                            type=ProductAnalyticsRetentionCalendarTimeIntervalType.CALENDAR,
                            value=ProductAnalyticsCalendarInterval(
                                alignment="monday",
                                quantity=1,
                                timezone="UTC",
                                type=ProductAnalyticsCalendarIntervalType.WEEK,
                            ),
                        ),
                    ),
                ),
            ),
            to=1756857600000,
        ),
        type=ProductAnalyticsRetentionListRequestType.RETENTION_LIST_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_product_analytics_retention_list"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_retention_list(body=body)

    print(response)
