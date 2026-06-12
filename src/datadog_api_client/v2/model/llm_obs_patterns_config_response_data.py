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
    from datadog_api_client.v2.model.llm_obs_patterns_config_attributes import LLMObsPatternsConfigAttributes
    from datadog_api_client.v2.model.llm_obs_patterns_config_type import LLMObsPatternsConfigType


class LLMObsPatternsConfigResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_config_attributes import LLMObsPatternsConfigAttributes
        from datadog_api_client.v2.model.llm_obs_patterns_config_type import LLMObsPatternsConfigType

        return {
            "attributes": (LLMObsPatternsConfigAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsPatternsConfigAttributes, id: str, type: LLMObsPatternsConfigType, **kwargs):
        """
        Data object of an LLM Observability patterns configuration.

        :param attributes: Attributes of an LLM Observability patterns configuration.
        :type attributes: LLMObsPatternsConfigAttributes

        :param id: Unique identifier of the configuration.
        :type id: str

        :param type: Resource type of an LLM Observability patterns configuration.
        :type type: LLMObsPatternsConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
