"""
Aggregate LLM Observability experimentation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_aggregate import (
    LLMObsExperimentationAnalyticsAggregate,
)
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_compute import LLMObsExperimentationAnalyticsCompute
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_attributes_request import (
    LLMObsExperimentationAnalyticsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_request import (
    LLMObsExperimentationAnalyticsDataRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_group_by import LLMObsExperimentationAnalyticsGroupBy
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_request import LLMObsExperimentationAnalyticsRequest
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_search import LLMObsExperimentationAnalyticsSearch
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_time_range import (
    LLMObsExperimentationAnalyticsTimeRange,
)
from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType

body = LLMObsExperimentationAnalyticsRequest(
    data=LLMObsExperimentationAnalyticsDataRequest(
        attributes=LLMObsExperimentationAnalyticsDataAttributesRequest(
            aggregate=LLMObsExperimentationAnalyticsAggregate(
                compute=[
                    LLMObsExperimentationAnalyticsCompute(
                        metric="score_value",
                        name="avg_faithfulness",
                    ),
                ],
                dataset_version=None,
                group_by=[
                    LLMObsExperimentationAnalyticsGroupBy(
                        field="span_id",
                    ),
                ],
                indexes=[
                    "experiment-evals",
                ],
                limit=1000,
                search=LLMObsExperimentationAnalyticsSearch(
                    query="@experiment_id:3fd6b5e0-8910-4b1c-a7d0-5b84de329012",
                ),
                time=LLMObsExperimentationAnalyticsTimeRange(
                    _from=1705312200000,
                    to=1705315800000,
                ),
            ),
        ),
        type=LLMObsExperimentationType.EXPERIMENTATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["aggregate_llm_obs_experimentation"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.aggregate_llm_obs_experimentation(body=body)

    print(response)
