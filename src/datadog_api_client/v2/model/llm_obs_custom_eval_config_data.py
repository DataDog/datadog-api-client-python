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
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_attributes import LLMObsCustomEvalConfigAttributes
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_type import LLMObsCustomEvalConfigType


class LLMObsCustomEvalConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_attributes import LLMObsCustomEvalConfigAttributes
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_type import LLMObsCustomEvalConfigType

        return {
            "attributes": (LLMObsCustomEvalConfigAttributes,),
            "id": (str,),
            "type": (LLMObsCustomEvalConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsCustomEvalConfigAttributes, id: str, type: LLMObsCustomEvalConfigType, **kwargs
    ):
        """
        Data object for a custom LLM Observability evaluator configuration.

        :param attributes: Attributes of a custom LLM Observability evaluator configuration.
        :type attributes: LLMObsCustomEvalConfigAttributes

        :param id: Unique name identifier of the evaluator configuration.
        :type id: str

        :param type: Type of the custom LLM Observability evaluator configuration resource.
        :type type: LLMObsCustomEvalConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
