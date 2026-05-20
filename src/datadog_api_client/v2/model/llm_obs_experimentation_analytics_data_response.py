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
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_attributes_response import (
        LLMObsExperimentationAnalyticsDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType


class LLMObsExperimentationAnalyticsDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_data_attributes_response import (
            LLMObsExperimentationAnalyticsDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType

        return {
            "attributes": (LLMObsExperimentationAnalyticsDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsExperimentationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsExperimentationAnalyticsDataAttributesResponse,
        id: str,
        type: LLMObsExperimentationType,
        **kwargs,
    ):
        """
        JSON:API data object for an analytics response.

        :param attributes: Attributes of an analytics response.
        :type attributes: LLMObsExperimentationAnalyticsDataAttributesResponse

        :param id: Server-generated identifier for this analytics result.
        :type id: str

        :param type: Resource type for experimentation search and analytics operations.
        :type type: LLMObsExperimentationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
