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
    from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_attributes_request import (
        LLMObsExperimentationSimpleSearchDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType


class LLMObsExperimentationSimpleSearchDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_attributes_request import (
            LLMObsExperimentationSimpleSearchDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType

        return {
            "attributes": (LLMObsExperimentationSimpleSearchDataAttributesRequest,),
            "type": (LLMObsExperimentationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsExperimentationSimpleSearchDataAttributesRequest,
        type: LLMObsExperimentationType,
        **kwargs,
    ):
        """
        Data object for an experimentation simple search request.

        :param attributes: Attributes for an experimentation simple search request.
        :type attributes: LLMObsExperimentationSimpleSearchDataAttributesRequest

        :param type: Resource type for experimentation search and analytics operations.
        :type type: LLMObsExperimentationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
