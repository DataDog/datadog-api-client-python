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
    from datadog_api_client.v2.model.llm_obs_patterns_config_upsert_request_attributes import (
        LLMObsPatternsConfigUpsertRequestAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_config_type import LLMObsPatternsConfigType


class LLMObsPatternsConfigUpsertRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_config_upsert_request_attributes import (
            LLMObsPatternsConfigUpsertRequestAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_config_type import LLMObsPatternsConfigType

        return {
            "attributes": (LLMObsPatternsConfigUpsertRequestAttributes,),
            "type": (LLMObsPatternsConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsPatternsConfigUpsertRequestAttributes, type: LLMObsPatternsConfigType, **kwargs
    ):
        """
        Data object for creating or updating an LLM Observability patterns configuration.

        :param attributes: Attributes for creating or updating an LLM Observability patterns configuration.
        :type attributes: LLMObsPatternsConfigUpsertRequestAttributes

        :param type: Resource type of an LLM Observability patterns configuration.
        :type type: LLMObsPatternsConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
