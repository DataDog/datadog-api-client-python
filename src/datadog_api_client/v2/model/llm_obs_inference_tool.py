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
    from datadog_api_client.v2.model.llm_obs_inference_function import LLMObsInferenceFunction


class LLMObsInferenceTool(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_inference_function import LLMObsInferenceFunction

        return {
            "function": (LLMObsInferenceFunction,),
            "type": (str,),
        }

    attribute_map = {
        "function": "function",
        "type": "type",
    }

    def __init__(self_, function: LLMObsInferenceFunction, type: str, **kwargs):
        """
        A tool definition available to the model during inference.

        :param function: A function definition for a tool available to the model.
        :type function: LLMObsInferenceFunction

        :param type: The type of tool.
        :type type: str
        """
        super().__init__(kwargs)

        self_.function = function
        self_.type = type
