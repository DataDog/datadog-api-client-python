# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experiment_metric import LLMObsExperimentMetric
    from datadog_api_client.v2.model.llm_obs_experiment_span import LLMObsExperimentSpan


class LLMObsExperimentEventsDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_metric import LLMObsExperimentMetric
        from datadog_api_client.v2.model.llm_obs_experiment_span import LLMObsExperimentSpan

        return {
            "metrics": ([LLMObsExperimentMetric],),
            "spans": ([LLMObsExperimentSpan],),
        }

    attribute_map = {
        "metrics": "metrics",
        "spans": "spans",
    }

    def __init__(
        self_,
        metrics: Union[List[LLMObsExperimentMetric], UnsetType] = unset,
        spans: Union[List[LLMObsExperimentSpan], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for pushing experiment events including spans and metrics.

        :param metrics: List of metrics to push for the experiment.
        :type metrics: [LLMObsExperimentMetric], optional

        :param spans: List of spans to push for the experiment.
        :type spans: [LLMObsExperimentSpan], optional
        """
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if spans is not unset:
            kwargs["spans"] = spans
        super().__init__(kwargs)
