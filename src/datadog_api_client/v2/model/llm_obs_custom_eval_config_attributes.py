# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_user import LLMObsCustomEvalConfigUser
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_judge_config import (
        LLMObsCustomEvalConfigLLMJudgeConfig,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_provider import LLMObsCustomEvalConfigLLMProvider
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_target import LLMObsCustomEvalConfigTarget


class LLMObsCustomEvalConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_user import LLMObsCustomEvalConfigUser
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_judge_config import (
            LLMObsCustomEvalConfigLLMJudgeConfig,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_provider import (
            LLMObsCustomEvalConfigLLMProvider,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_target import LLMObsCustomEvalConfigTarget

        return {
            "category": (str,),
            "created_at": (datetime,),
            "created_by": (LLMObsCustomEvalConfigUser,),
            "eval_name": (str,),
            "last_updated_by": (LLMObsCustomEvalConfigUser,),
            "llm_judge_config": (LLMObsCustomEvalConfigLLMJudgeConfig,),
            "llm_provider": (LLMObsCustomEvalConfigLLMProvider,),
            "target": (LLMObsCustomEvalConfigTarget,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "category": "category",
        "created_at": "created_at",
        "created_by": "created_by",
        "eval_name": "eval_name",
        "last_updated_by": "last_updated_by",
        "llm_judge_config": "llm_judge_config",
        "llm_provider": "llm_provider",
        "target": "target",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        eval_name: str,
        updated_at: datetime,
        category: Union[str, UnsetType] = unset,
        created_by: Union[LLMObsCustomEvalConfigUser, UnsetType] = unset,
        last_updated_by: Union[LLMObsCustomEvalConfigUser, UnsetType] = unset,
        llm_judge_config: Union[LLMObsCustomEvalConfigLLMJudgeConfig, UnsetType] = unset,
        llm_provider: Union[LLMObsCustomEvalConfigLLMProvider, UnsetType] = unset,
        target: Union[LLMObsCustomEvalConfigTarget, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a custom LLM Observability evaluator configuration.

        :param category: Category of the evaluator.
        :type category: str, optional

        :param created_at: Timestamp when the evaluator configuration was created.
        :type created_at: datetime

        :param created_by: A Datadog user associated with a custom evaluator configuration.
        :type created_by: LLMObsCustomEvalConfigUser, optional

        :param eval_name: Name of the custom evaluator.
        :type eval_name: str

        :param last_updated_by: A Datadog user associated with a custom evaluator configuration.
        :type last_updated_by: LLMObsCustomEvalConfigUser, optional

        :param llm_judge_config: LLM judge configuration for a custom evaluator.
        :type llm_judge_config: LLMObsCustomEvalConfigLLMJudgeConfig, optional

        :param llm_provider: LLM provider configuration for a custom evaluator.
        :type llm_provider: LLMObsCustomEvalConfigLLMProvider, optional

        :param target: Target application configuration for a custom evaluator.
        :type target: LLMObsCustomEvalConfigTarget, optional

        :param updated_at: Timestamp when the evaluator configuration was last updated.
        :type updated_at: datetime
        """
        if category is not unset:
            kwargs["category"] = category
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        if llm_judge_config is not unset:
            kwargs["llm_judge_config"] = llm_judge_config
        if llm_provider is not unset:
            kwargs["llm_provider"] = llm_provider
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.eval_name = eval_name
        self_.updated_at = updated_at
