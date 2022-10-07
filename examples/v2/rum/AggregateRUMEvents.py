"""
Aggregate RUM events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_aggregate_request import RUMAggregateRequest
from datadog_api_client.v2.model.rum_aggregation_function import RUMAggregationFunction
from datadog_api_client.v2.model.rum_compute import RUMCompute
from datadog_api_client.v2.model.rum_compute_type import RUMComputeType
from datadog_api_client.v2.model.rum_group_by import RUMGroupBy
from datadog_api_client.v2.model.rum_query_filter import RUMQueryFilter
from datadog_api_client.v2.model.rum_query_options import RUMQueryOptions
from datadog_api_client.v2.model.rum_query_page_options import RUMQueryPageOptions

body = RUMAggregateRequest(
    compute=[
        RUMCompute(
            aggregation=RUMAggregationFunction.PERCENTILE_90,
            metric="@view.time_spent",
            type=RUMComputeType.TOTAL,
        ),
    ],
    filter=RUMQueryFilter(
        _from="now-15m",
        query="@type:view AND @session.type:user",
        to="now",
    ),
    group_by=[
        RUMGroupBy(
            facet="@view.time_spent",
            limit=10,
            total=False,
        ),
    ],
    options=RUMQueryOptions(
        timezone="GMT",
    ),
    page=RUMQueryPageOptions(
        limit=25,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.aggregate_rum_events(body=body)

    print(response)
