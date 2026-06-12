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
    from datadog_api_client.v2.model.llm_obs_patterns_trigger_request_attributes import (
        LLMObsPatternsTriggerRequestAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_request_type import LLMObsPatternsRequestType


class LLMObsPatternsTriggerRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_trigger_request_attributes import (
            LLMObsPatternsTriggerRequestAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_request_type import LLMObsPatternsRequestType

        return {
            "attributes": (LLMObsPatternsTriggerRequestAttributes,),
            "type": (LLMObsPatternsRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsPatternsTriggerRequestAttributes, type: LLMObsPatternsRequestType, **kwargs):
        """
        Data object for triggering an LLM Observability patterns run.

        :param attributes: Attributes for triggering an LLM Observability patterns run.
        :type attributes: LLMObsPatternsTriggerRequestAttributes

        :param type: Resource type for triggering an LLM Observability patterns run.
        :type type: LLMObsPatternsRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
