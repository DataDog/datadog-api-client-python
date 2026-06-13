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
    from datadog_api_client.v2.model.llm_obs_patterns_configs_response_attributes import (
        LLMObsPatternsConfigsResponseAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_configs_list_type import LLMObsPatternsConfigsListType


class LLMObsPatternsConfigsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_configs_response_attributes import (
            LLMObsPatternsConfigsResponseAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_configs_list_type import LLMObsPatternsConfigsListType

        return {
            "attributes": (LLMObsPatternsConfigsResponseAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsConfigsListType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsPatternsConfigsResponseAttributes,
        id: str,
        type: LLMObsPatternsConfigsListType,
        **kwargs,
    ):
        """
        Data object of a list of LLM Observability patterns configurations.

        :param attributes: Attributes of a list of LLM Observability patterns configurations.
        :type attributes: LLMObsPatternsConfigsResponseAttributes

        :param id: Identifier of the list response.
        :type id: str

        :param type: Resource type of a list of LLM Observability patterns configurations.
        :type type: LLMObsPatternsConfigsListType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
