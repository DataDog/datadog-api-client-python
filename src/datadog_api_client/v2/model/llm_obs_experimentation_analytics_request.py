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
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_request import (
        LLMObsExperimentationAnalyticsDataRequest,
    )


class LLMObsExperimentationAnalyticsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_request import (
            LLMObsExperimentationAnalyticsDataRequest,
        )

        return {
            "data": (LLMObsExperimentationAnalyticsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsExperimentationAnalyticsDataRequest, **kwargs):
        """
        Request to run an analytics aggregation over LLM Observability experimentation data.

        :param data: Data object for an analytics request.
        :type data: LLMObsExperimentationAnalyticsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
