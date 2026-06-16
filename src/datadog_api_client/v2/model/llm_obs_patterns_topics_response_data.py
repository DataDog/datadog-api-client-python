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
    from datadog_api_client.v2.model.llm_obs_patterns_topics_response_attributes import (
        LLMObsPatternsTopicsResponseAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_topics_type import LLMObsPatternsTopicsType


class LLMObsPatternsTopicsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_topics_response_attributes import (
            LLMObsPatternsTopicsResponseAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_topics_type import LLMObsPatternsTopicsType

        return {
            "attributes": (LLMObsPatternsTopicsResponseAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsTopicsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsPatternsTopicsResponseAttributes, id: str, type: LLMObsPatternsTopicsType, **kwargs
    ):
        """
        Data object of an LLM Observability patterns topics response.

        :param attributes: Attributes of an LLM Observability patterns topics response.
        :type attributes: LLMObsPatternsTopicsResponseAttributes

        :param id: Identifier of the run the topics belong to.
        :type id: str

        :param type: Resource type of an LLM Observability patterns topics response.
        :type type: LLMObsPatternsTopicsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
