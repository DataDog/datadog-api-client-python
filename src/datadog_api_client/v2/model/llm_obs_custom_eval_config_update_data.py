# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_update_attributes import (
        LLMObsCustomEvalConfigUpdateAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_type import LLMObsCustomEvalConfigType


class LLMObsCustomEvalConfigUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_update_attributes import (
            LLMObsCustomEvalConfigUpdateAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_type import LLMObsCustomEvalConfigType

        return {
            "attributes": (LLMObsCustomEvalConfigUpdateAttributes,),
            "id": (str,),
            "type": (LLMObsCustomEvalConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsCustomEvalConfigUpdateAttributes,
        type: LLMObsCustomEvalConfigType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for creating or updating a custom LLM Observability evaluator configuration.

        :param attributes: Attributes for creating or updating a custom LLM Observability evaluator configuration.
        :type attributes: LLMObsCustomEvalConfigUpdateAttributes

        :param id: Name of the evaluator. If provided, must match the eval_name path parameter.
        :type id: str, optional

        :param type: Type of the custom LLM Observability evaluator configuration resource.
        :type type: LLMObsCustomEvalConfigType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
