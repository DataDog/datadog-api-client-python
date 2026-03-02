"""
Push events for an LLM Observability experiment returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_event_type import LLMObsEventType
from datadog_api_client.v2.model.llm_obs_experiment_events_data_attributes_request import (
    LLMObsExperimentEventsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_experiment_events_data_request import LLMObsExperimentEventsDataRequest
from datadog_api_client.v2.model.llm_obs_experiment_events_request import LLMObsExperimentEventsRequest
from datadog_api_client.v2.model.llm_obs_experiment_metric import LLMObsExperimentMetric
from datadog_api_client.v2.model.llm_obs_experiment_metric_error import LLMObsExperimentMetricError
from datadog_api_client.v2.model.llm_obs_experiment_span import LLMObsExperimentSpan
from datadog_api_client.v2.model.llm_obs_experiment_span_error import LLMObsExperimentSpanError
from datadog_api_client.v2.model.llm_obs_experiment_span_meta import LLMObsExperimentSpanMeta
from datadog_api_client.v2.model.llm_obs_metric_assessment import LLMObsMetricAssessment
from datadog_api_client.v2.model.llm_obs_metric_score_type import LLMObsMetricScoreType

body = LLMObsExperimentEventsRequest(
    data=LLMObsExperimentEventsDataRequest(
        attributes=LLMObsExperimentEventsDataAttributesRequest(
            metrics=[
                LLMObsExperimentMetric(
                    assessment=LLMObsMetricAssessment.PASS,
                    error=LLMObsExperimentMetricError(),
                    label="faithfulness",
                    metric_type=LLMObsMetricScoreType.SCORE,
                    span_id="span-7a1b2c3d",
                    tags=[],
                    timestamp_ms=1705314600000,
                ),
            ],
            spans=[
                LLMObsExperimentSpan(
                    dataset_id="9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d",
                    duration=1500000000,
                    meta=LLMObsExperimentSpanMeta(
                        error=LLMObsExperimentSpanError(),
                        input=None,
                        output=None,
                    ),
                    name="llm_call",
                    project_id="a33671aa-24fd-4dcd-9b33-a8ec7dde7751",
                    span_id="span-7a1b2c3d",
                    start_ns=1705314600000000000,
                    status="ok",
                    tags=[],
                    trace_id="abc123def456",
                ),
            ],
        ),
        type=LLMObsEventType.EVENTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_experiment_events"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.create_llm_obs_experiment_events(experiment_id="experiment_id", body=body)
