"""
Aggregate tests events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi
from datadog_api_client.v2.model.ci_app_aggregate_sort import CIAppAggregateSort
from datadog_api_client.v2.model.ci_app_aggregation_function import CIAppAggregationFunction
from datadog_api_client.v2.model.ci_app_compute import CIAppCompute
from datadog_api_client.v2.model.ci_app_compute_type import CIAppComputeType
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort_order import CIAppSortOrder
from datadog_api_client.v2.model.ci_app_tests_aggregate_request import CIAppTestsAggregateRequest
from datadog_api_client.v2.model.ci_app_tests_group_by import CIAppTestsGroupBy
from datadog_api_client.v2.model.ci_app_tests_query_filter import CIAppTestsQueryFilter

body = CIAppTestsAggregateRequest(
    compute=[
        CIAppCompute(
            aggregation=CIAppAggregationFunction.COUNT,
            metric="@test.is_flaky",
            type=CIAppComputeType.TOTAL,
        ),
    ],
    filter=CIAppTestsQueryFilter(
        _from="now-15m",
        query="@language:(python OR go)",
        to="now",
    ),
    group_by=[
        CIAppTestsGroupBy(
            facet="@git.branch",
            limit=10,
            sort=CIAppAggregateSort(
                order=CIAppSortOrder.ASCENDING,
            ),
            total=False,
        ),
    ],
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
    page=CIAppQueryPageOptions(
        limit=25,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    response = api_instance.aggregate_ci_app_test_events(body=body)

    print(response)
