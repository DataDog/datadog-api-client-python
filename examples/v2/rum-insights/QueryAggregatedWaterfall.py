"""
Query aggregated waterfall returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_insights_api import RUMInsightsApi
from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import AggregatedWaterfallPerformanceCriteria
from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria_metric import (
    AggregatedWaterfallPerformanceCriteriaMetric,
)
from datadog_api_client.v2.model.aggregated_waterfall_request import AggregatedWaterfallRequest
from datadog_api_client.v2.model.aggregated_waterfall_request_attributes import AggregatedWaterfallRequestAttributes
from datadog_api_client.v2.model.aggregated_waterfall_request_data import AggregatedWaterfallRequestData
from datadog_api_client.v2.model.aggregated_waterfall_request_type import AggregatedWaterfallRequestType

body = AggregatedWaterfallRequest(
    data=AggregatedWaterfallRequestData(
        attributes=AggregatedWaterfallRequestAttributes(
            application_id="ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b",
            criteria=AggregatedWaterfallPerformanceCriteria(
                max=5.0,
                metric=AggregatedWaterfallPerformanceCriteriaMetric.LARGEST_CONTENTFUL_PAINT,
                min=2.5,
            ),
            filter="@session.type:user",
            _from=1762437564,
            include_global_appearance=False,
            sample_size=20,
            to=1762523964,
            view_name="/account/login(/:type)",
        ),
        type=AggregatedWaterfallRequestType.AGGREGATED_WATERFALL,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_aggregated_waterfall"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMInsightsApi(api_client)
    response = api_instance.query_aggregated_waterfall(body=body)

    print(response)
