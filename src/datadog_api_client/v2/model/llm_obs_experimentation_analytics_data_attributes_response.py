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
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_result import (
        LLMObsExperimentationAnalyticsResult,
    )


class LLMObsExperimentationAnalyticsDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_result import (
            LLMObsExperimentationAnalyticsResult,
        )

        return {
            "hit_count": (int,),
            "result": (LLMObsExperimentationAnalyticsResult,),
        }

    attribute_map = {
        "hit_count": "hit_count",
        "result": "result",
    }

    def __init__(self_, hit_count: int, result: LLMObsExperimentationAnalyticsResult, **kwargs):
        """
        Attributes of an analytics response.

        :param hit_count: Total number of events matched by the query before grouping.
        :type hit_count: int

        :param result: Analytics query result containing all buckets.
        :type result: LLMObsExperimentationAnalyticsResult
        """
        super().__init__(kwargs)

        self_.hit_count = hit_count
        self_.result = result
