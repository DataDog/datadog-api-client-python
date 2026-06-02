"""
Query aggregated long tasks returns "Successful response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_insights_api import RUMInsightsApi
from datadog_api_client.v2.model.aggregated_long_tasks_request import AggregatedLongTasksRequest
from datadog_api_client.v2.model.aggregated_long_tasks_request_attributes import AggregatedLongTasksRequestAttributes
from datadog_api_client.v2.model.aggregated_long_tasks_request_data import AggregatedLongTasksRequestData
from datadog_api_client.v2.model.aggregated_long_tasks_request_type import AggregatedLongTasksRequestType
from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import AggregatedWaterfallPerformanceCriteria
from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria_metric import (
    AggregatedWaterfallPerformanceCriteriaMetric,
)

body = AggregatedLongTasksRequest(
    data=AggregatedLongTasksRequestData(
        attributes=AggregatedLongTasksRequestAttributes(
            application_id="ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b",
            criteria=AggregatedWaterfallPerformanceCriteria(
                max=5.0,
                metric=AggregatedWaterfallPerformanceCriteriaMetric.LARGEST_CONTENTFUL_PAINT,
                min=2.5,
            ),
            filter="@session.type:user",
            _from=1762437564,
            sample_size=20,
            to=1762523964,
            view_name="/account/login(/:type)",
        ),
        type=AggregatedLongTasksRequestType.AGGREGATED_LONG_TASKS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_aggregated_long_tasks"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMInsightsApi(api_client)
    response = api_instance.query_aggregated_long_tasks(body=body)

    print(response)
