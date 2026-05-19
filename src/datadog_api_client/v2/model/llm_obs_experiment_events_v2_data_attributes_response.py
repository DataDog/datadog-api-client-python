# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experiment_span_with_evals import LLMObsExperimentSpanWithEvals
    from datadog_api_client.v2.model.llm_obs_experiment_eval_metric_event import LLMObsExperimentEvalMetricEvent


class LLMObsExperimentEventsV2DataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_span_with_evals import LLMObsExperimentSpanWithEvals
        from datadog_api_client.v2.model.llm_obs_experiment_eval_metric_event import LLMObsExperimentEvalMetricEvent

        return {
            "spans": ([LLMObsExperimentSpanWithEvals],),
            "summary_metrics": ([LLMObsExperimentEvalMetricEvent],),
        }

    attribute_map = {
        "spans": "spans",
        "summary_metrics": "summary_metrics",
    }

    def __init__(
        self_,
        spans: List[LLMObsExperimentSpanWithEvals],
        summary_metrics: List[LLMObsExperimentEvalMetricEvent],
        **kwargs,
    ):
        """
        Attributes of an experiment events response.

        :param spans: Experiment spans, each enriched with their associated evaluation metrics.
        :type spans: [LLMObsExperimentSpanWithEvals]

        :param summary_metrics: Experiment-level summary evaluation metrics (not tied to individual spans).
        :type summary_metrics: [LLMObsExperimentEvalMetricEvent]
        """
        super().__init__(kwargs)

        self_.spans = spans
        self_.summary_metrics = summary_metrics
