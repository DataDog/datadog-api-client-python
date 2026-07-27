# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_assessment_criteria import (
        LLMObsCustomEvalConfigAssessmentCriteria,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_inference_params import (
        LLMObsCustomEvalConfigInferenceParams,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_parsing_type import LLMObsCustomEvalConfigParsingType
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_message import (
        LLMObsCustomEvalConfigPromptMessage,
    )


class LLMObsCustomEvalConfigLLMJudgeConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_assessment_criteria import (
            LLMObsCustomEvalConfigAssessmentCriteria,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_inference_params import (
            LLMObsCustomEvalConfigInferenceParams,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_parsing_type import (
            LLMObsCustomEvalConfigParsingType,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_message import (
            LLMObsCustomEvalConfigPromptMessage,
        )

        return {
            "assessment_criteria": (LLMObsCustomEvalConfigAssessmentCriteria,),
            "context_query": (str, none_type),
            "inference_params": (LLMObsCustomEvalConfigInferenceParams,),
            "last_used_library_prompt_template_name": (str, none_type),
            "modified_library_prompt_template": (bool, none_type),
            "output_schema": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
            "parsing_type": (LLMObsCustomEvalConfigParsingType,),
            "prompt_template": ([LLMObsCustomEvalConfigPromptMessage],),
            "target_query": (str, none_type),
            "user_specified_json_post_processing_function": (str, none_type),
        }

    attribute_map = {
        "assessment_criteria": "assessment_criteria",
        "context_query": "context_query",
        "inference_params": "inference_params",
        "last_used_library_prompt_template_name": "last_used_library_prompt_template_name",
        "modified_library_prompt_template": "modified_library_prompt_template",
        "output_schema": "output_schema",
        "parsing_type": "parsing_type",
        "prompt_template": "prompt_template",
        "target_query": "target_query",
        "user_specified_json_post_processing_function": "user_specified_json_post_processing_function",
    }

    def __init__(
        self_,
        inference_params: LLMObsCustomEvalConfigInferenceParams,
        assessment_criteria: Union[LLMObsCustomEvalConfigAssessmentCriteria, UnsetType] = unset,
        context_query: Union[str, none_type, UnsetType] = unset,
        last_used_library_prompt_template_name: Union[str, none_type, UnsetType] = unset,
        modified_library_prompt_template: Union[bool, none_type, UnsetType] = unset,
        output_schema: Union[Dict[str, Any], none_type, UnsetType] = unset,
        parsing_type: Union[LLMObsCustomEvalConfigParsingType, UnsetType] = unset,
        prompt_template: Union[List[LLMObsCustomEvalConfigPromptMessage], UnsetType] = unset,
        target_query: Union[str, none_type, UnsetType] = unset,
        user_specified_json_post_processing_function: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        LLM judge configuration for a custom evaluator.

        :param assessment_criteria: Criteria used to assess the pass/fail result of a custom evaluator.
        :type assessment_criteria: LLMObsCustomEvalConfigAssessmentCriteria, optional

        :param context_query: Query used to extract additional context for the evaluation.
        :type context_query: str, none_type, optional

        :param inference_params: LLM inference parameters for a custom evaluator.
        :type inference_params: LLMObsCustomEvalConfigInferenceParams

        :param last_used_library_prompt_template_name: Name of the last library prompt template used.
        :type last_used_library_prompt_template_name: str, none_type, optional

        :param modified_library_prompt_template: Whether the library prompt template was modified.
        :type modified_library_prompt_template: bool, none_type, optional

        :param output_schema: JSON schema describing the expected output format of the LLM judge.
        :type output_schema: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param parsing_type: Output parsing type for a custom LLM judge evaluator.
        :type parsing_type: LLMObsCustomEvalConfigParsingType, optional

        :param prompt_template: List of messages forming the LLM judge prompt template.
        :type prompt_template: [LLMObsCustomEvalConfigPromptMessage], optional

        :param target_query: Query used to extract the target value to evaluate.
        :type target_query: str, none_type, optional

        :param user_specified_json_post_processing_function: User-provided function applied to post-process the JSON output of the LLM judge.
        :type user_specified_json_post_processing_function: str, none_type, optional
        """
        if assessment_criteria is not unset:
            kwargs["assessment_criteria"] = assessment_criteria
        if context_query is not unset:
            kwargs["context_query"] = context_query
        if last_used_library_prompt_template_name is not unset:
            kwargs["last_used_library_prompt_template_name"] = last_used_library_prompt_template_name
        if modified_library_prompt_template is not unset:
            kwargs["modified_library_prompt_template"] = modified_library_prompt_template
        if output_schema is not unset:
            kwargs["output_schema"] = output_schema
        if parsing_type is not unset:
            kwargs["parsing_type"] = parsing_type
        if prompt_template is not unset:
            kwargs["prompt_template"] = prompt_template
        if target_query is not unset:
            kwargs["target_query"] = target_query
        if user_specified_json_post_processing_function is not unset:
            kwargs["user_specified_json_post_processing_function"] = user_specified_json_post_processing_function
        super().__init__(kwargs)

        self_.inference_params = inference_params
