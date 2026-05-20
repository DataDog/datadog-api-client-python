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
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_response import (
        LLMObsExperimentationAnalyticsDataResponse,
    )


class LLMObsExperimentationAnalyticsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_response import (
            LLMObsExperimentationAnalyticsDataResponse,
        )

        return {
            "data": (LLMObsExperimentationAnalyticsDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsExperimentationAnalyticsDataResponse, **kwargs):
        """
        Response to an analytics query.

        :param data: JSON:API data object for an analytics response.
        :type data: LLMObsExperimentationAnalyticsDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
