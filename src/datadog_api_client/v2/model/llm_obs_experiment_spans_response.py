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
    from datadog_api_client.v2.model.llm_obs_experiment_span_data_response import LLMObsExperimentSpanDataResponse


class LLMObsExperimentSpansResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_span_data_response import LLMObsExperimentSpanDataResponse

        return {
            "data": ([LLMObsExperimentSpanDataResponse],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[LLMObsExperimentSpanDataResponse], **kwargs):
        """
        Response for listing experiment spans (v1). Returns only spans with their evaluation metrics. No summary metrics or pagination are included. Deprecated in favor of ``ListLLMObsExperimentEventsV3``.

        :param data: List of experiment spans with their evaluation metrics.
        :type data: [LLMObsExperimentSpanDataResponse]
        """
        super().__init__(kwargs)

        self_.data = data
