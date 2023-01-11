"""
Aggregate pipelines events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_aggregation_function import CIAppAggregationFunction
from datadog_api_client.v2.model.ci_app_compute import CIAppCompute
from datadog_api_client.v2.model.ci_app_compute_type import CIAppComputeType
from datadog_api_client.v2.model.ci_app_pipelines_aggregate_request import CIAppPipelinesAggregateRequest
from datadog_api_client.v2.model.ci_app_pipelines_group_by import CIAppPipelinesGroupBy
from datadog_api_client.v2.model.ci_app_pipelines_query_filter import CIAppPipelinesQueryFilter
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions

body = CIAppPipelinesAggregateRequest(
    compute=[
        CIAppCompute(
            aggregation=CIAppAggregationFunction.PERCENTILE_90,
            metric="@duration",
            type=CIAppComputeType.TOTAL,
        ),
    ],
    filter=CIAppPipelinesQueryFilter(
        _from="now-15m",
        query="@ci.provider.name:(gitlab OR github)",
        to="now",
    ),
    group_by=[
        CIAppPipelinesGroupBy(
            facet="@ci.status",
            limit=10,
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
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.aggregate_ci_app_pipeline_events(body=body)

    print(response)
