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
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_data import LLMObsCustomEvalConfigData


class LLMObsCustomEvalConfigResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_data import LLMObsCustomEvalConfigData

        return {
            "data": (LLMObsCustomEvalConfigData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsCustomEvalConfigData, **kwargs):
        """
        Response containing a custom LLM Observability evaluator configuration.

        :param data: Data object for a custom LLM Observability evaluator configuration.
        :type data: LLMObsCustomEvalConfigData
        """
        super().__init__(kwargs)

        self_.data = data
