"""
Aggregate spans returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi
from datadog_api_client.v2.model.spans_aggregate_request import SpansAggregateRequestJSON
from datadog_api_client.v2.model.spans_aggregation_function import SpansAggregationFunction
from datadog_api_client.v2.model.spans_compute import SpansCompute
from datadog_api_client.v2.model.spans_compute_type import SpansComputeType
from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

body = SpansAggregateRequestJSON(
    compute=[
        SpansCompute(
            aggregation=SpansAggregationFunction.COUNT,
            interval="5m",
            type=SpansComputeType.TIMESERIES,
        ),
    ],
    filter=SpansQueryFilter(
        _from="now-15m",
        query="*",
        to="now",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    response = api_instance.aggregate_spans(body=body)

    print(response)
