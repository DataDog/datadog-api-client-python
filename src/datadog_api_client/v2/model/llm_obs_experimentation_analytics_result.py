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
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_value import LLMObsExperimentationAnalyticsValue


class LLMObsExperimentationAnalyticsResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_value import (
            LLMObsExperimentationAnalyticsValue,
        )

        return {
            "values": ([LLMObsExperimentationAnalyticsValue],),
        }

    attribute_map = {
        "values": "values",
    }

    def __init__(self_, values: List[LLMObsExperimentationAnalyticsValue], **kwargs):
        """
        Analytics query result containing all buckets.

        :param values: List of result buckets.
        :type values: [LLMObsExperimentationAnalyticsValue]
        """
        super().__init__(kwargs)

        self_.values = values
