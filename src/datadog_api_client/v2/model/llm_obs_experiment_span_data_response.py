# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experiment_span_with_evals import LLMObsExperimentSpanWithEvals
    from datadog_api_client.v2.model.llm_obs_experiment_span_type import LLMObsExperimentSpanType


class LLMObsExperimentSpanDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_span_with_evals import LLMObsExperimentSpanWithEvals
        from datadog_api_client.v2.model.llm_obs_experiment_span_type import LLMObsExperimentSpanType

        return {
            "attributes": (LLMObsExperimentSpanWithEvals,),
            "id": (str,),
            "type": (LLMObsExperimentSpanType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsExperimentSpanWithEvals, id: str, type: LLMObsExperimentSpanType, **kwargs):
        """
        JSON:API data item wrapping a single experiment span with evaluations.

        :param attributes: An experiment span enriched with its associated evaluation metrics.
        :type attributes: LLMObsExperimentSpanWithEvals

        :param id: Unique identifier of the span.
        :type id: str

        :param type: Resource type for a span item in an experiment spans response.
        :type type: LLMObsExperimentSpanType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
