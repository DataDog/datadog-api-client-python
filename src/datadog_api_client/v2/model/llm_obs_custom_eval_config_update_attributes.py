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
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_judge_config import (
        LLMObsCustomEvalConfigLLMJudgeConfig,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_provider import LLMObsCustomEvalConfigLLMProvider
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_target import LLMObsCustomEvalConfigTarget


class LLMObsCustomEvalConfigUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_judge_config import (
            LLMObsCustomEvalConfigLLMJudgeConfig,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_provider import (
            LLMObsCustomEvalConfigLLMProvider,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_target import LLMObsCustomEvalConfigTarget

        return {
            "category": (str,),
            "eval_name": (str,),
            "llm_judge_config": (LLMObsCustomEvalConfigLLMJudgeConfig,),
            "llm_provider": (LLMObsCustomEvalConfigLLMProvider,),
            "target": (LLMObsCustomEvalConfigTarget,),
        }

    attribute_map = {
        "category": "category",
        "eval_name": "eval_name",
        "llm_judge_config": "llm_judge_config",
        "llm_provider": "llm_provider",
        "target": "target",
    }

    def __init__(
        self_,
        target: LLMObsCustomEvalConfigTarget,
        category: Union[str, UnsetType] = unset,
        eval_name: Union[str, UnsetType] = unset,
        llm_judge_config: Union[LLMObsCustomEvalConfigLLMJudgeConfig, UnsetType] = unset,
        llm_provider: Union[LLMObsCustomEvalConfigLLMProvider, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a custom LLM Observability evaluator configuration.

        :param category: Category of the evaluator.
        :type category: str, optional

        :param eval_name: Name of the custom evaluator. If provided, must match the eval_name path parameter.
        :type eval_name: str, optional

        :param llm_judge_config: LLM judge configuration for a custom evaluator.
        :type llm_judge_config: LLMObsCustomEvalConfigLLMJudgeConfig, optional

        :param llm_provider: LLM provider configuration for a custom evaluator.
        :type llm_provider: LLMObsCustomEvalConfigLLMProvider, optional

        :param target: Target application configuration for a custom evaluator.
        :type target: LLMObsCustomEvalConfigTarget
        """
        if category is not unset:
            kwargs["category"] = category
        if eval_name is not unset:
            kwargs["eval_name"] = eval_name
        if llm_judge_config is not unset:
            kwargs["llm_judge_config"] = llm_judge_config
        if llm_provider is not unset:
            kwargs["llm_provider"] = llm_provider
        super().__init__(kwargs)

        self_.target = target
