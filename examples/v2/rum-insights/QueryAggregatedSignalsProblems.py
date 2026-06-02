"""
Query aggregated signals and problems returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_insights_api import RUMInsightsApi
from datadog_api_client.v2.model.aggregated_signals_problems_request import AggregatedSignalsProblemsRequest
from datadog_api_client.v2.model.aggregated_signals_problems_request_attributes import (
    AggregatedSignalsProblemsRequestAttributes,
)
from datadog_api_client.v2.model.aggregated_signals_problems_request_data import AggregatedSignalsProblemsRequestData
from datadog_api_client.v2.model.aggregated_signals_problems_request_type import AggregatedSignalsProblemsRequestType
from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import AggregatedWaterfallPerformanceCriteria
from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria_metric import (
    AggregatedWaterfallPerformanceCriteriaMetric,
)

body = AggregatedSignalsProblemsRequest(
    data=AggregatedSignalsProblemsRequestData(
        attributes=AggregatedSignalsProblemsRequestAttributes(
            application_id="ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b",
            criteria=AggregatedWaterfallPerformanceCriteria(
                max=5.0,
                metric=AggregatedWaterfallPerformanceCriteriaMetric.LARGEST_CONTENTFUL_PAINT,
                min=2.5,
            ),
            detection_types=[
                "high_script_evaluations",
                "uncompressed_resources",
            ],
            filter="@session.type:user",
            _from=1762437564,
            sample_size=30,
            to=1762523964,
            view_name="/account/login(/:type)",
        ),
        type=AggregatedSignalsProblemsRequestType.AGGREGATED_SIGNALS_PROBLEMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_aggregated_signals_problems"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMInsightsApi(api_client)
    response = api_instance.query_aggregated_signals_problems(body=body)

    print(response)
