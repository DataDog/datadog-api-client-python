"""
Create or update a custom evaluator configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_custom_eval_config_assessment_criteria import (
    LLMObsCustomEvalConfigAssessmentCriteria,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_bedrock_options import LLMObsCustomEvalConfigBedrockOptions
from datadog_api_client.v2.model.llm_obs_custom_eval_config_eval_scope import LLMObsCustomEvalConfigEvalScope
from datadog_api_client.v2.model.llm_obs_custom_eval_config_inference_params import (
    LLMObsCustomEvalConfigInferenceParams,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_integration_provider import (
    LLMObsCustomEvalConfigIntegrationProvider,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_judge_config import LLMObsCustomEvalConfigLLMJudgeConfig
from datadog_api_client.v2.model.llm_obs_custom_eval_config_llm_provider import LLMObsCustomEvalConfigLLMProvider
from datadog_api_client.v2.model.llm_obs_custom_eval_config_parsing_type import LLMObsCustomEvalConfigParsingType
from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_content import LLMObsCustomEvalConfigPromptContent
from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_content_value import (
    LLMObsCustomEvalConfigPromptContentValue,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_message import LLMObsCustomEvalConfigPromptMessage
from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_tool_call import LLMObsCustomEvalConfigPromptToolCall
from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_tool_result import (
    LLMObsCustomEvalConfigPromptToolResult,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_target import LLMObsCustomEvalConfigTarget
from datadog_api_client.v2.model.llm_obs_custom_eval_config_type import LLMObsCustomEvalConfigType
from datadog_api_client.v2.model.llm_obs_custom_eval_config_update_attributes import (
    LLMObsCustomEvalConfigUpdateAttributes,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_update_data import LLMObsCustomEvalConfigUpdateData
from datadog_api_client.v2.model.llm_obs_custom_eval_config_update_request import LLMObsCustomEvalConfigUpdateRequest
from datadog_api_client.v2.model.llm_obs_custom_eval_config_vertex_ai_options import (
    LLMObsCustomEvalConfigVertexAIOptions,
)

body = LLMObsCustomEvalConfigUpdateRequest(
    data=LLMObsCustomEvalConfigUpdateData(
        attributes=LLMObsCustomEvalConfigUpdateAttributes(
            category="Custom",
            eval_name="my-custom-evaluator",
            llm_judge_config=LLMObsCustomEvalConfigLLMJudgeConfig(
                assessment_criteria=LLMObsCustomEvalConfigAssessmentCriteria(
                    max_threshold=1.0,
                    min_threshold=0.7,
                    pass_values=[
                        "pass",
                        "yes",
                    ],
                    pass_when=True,
                ),
                inference_params=LLMObsCustomEvalConfigInferenceParams(
                    frequency_penalty=0.0,
                    max_tokens=1024,
                    presence_penalty=0.0,
                    temperature=0.7,
                    top_k=50,
                    top_p=1.0,
                ),
                last_used_library_prompt_template_name="sentiment-analysis-v1",
                modified_library_prompt_template=False,
                output_schema=None,
                parsing_type=LLMObsCustomEvalConfigParsingType.STRUCTURED_OUTPUT,
                prompt_template=[
                    LLMObsCustomEvalConfigPromptMessage(
                        content="Rate the quality of the following response:",
                        contents=[
                            LLMObsCustomEvalConfigPromptContent(
                                type="text",
                                value=LLMObsCustomEvalConfigPromptContentValue(
                                    text="What is the sentiment of this review?",
                                    tool_call=LLMObsCustomEvalConfigPromptToolCall(
                                        arguments='{"location": "San Francisco"}',
                                        id="call_abc123",
                                        name="get_weather",
                                        type="function",
                                    ),
                                    tool_call_result=LLMObsCustomEvalConfigPromptToolResult(
                                        name="get_weather",
                                        result="sunny, 72F",
                                        tool_id="call_abc123",
                                        type="function",
                                    ),
                                ),
                            ),
                        ],
                        role="user",
                    ),
                ],
            ),
            llm_provider=LLMObsCustomEvalConfigLLMProvider(
                bedrock=LLMObsCustomEvalConfigBedrockOptions(
                    region="us-east-1",
                ),
                integration_account_id="my-account-id",
                integration_provider=LLMObsCustomEvalConfigIntegrationProvider.OPENAI,
                model_name="gpt-4o",
                vertex_ai=LLMObsCustomEvalConfigVertexAIOptions(
                    location="us-central1",
                    project="my-gcp-project",
                ),
            ),
            target=LLMObsCustomEvalConfigTarget(
                application_name="my-llm-app",
                enabled=True,
                eval_scope=LLMObsCustomEvalConfigEvalScope.SPAN,
                filter="@service:my-service",
                root_spans_only=True,
                sampling_percentage=50.0,
            ),
        ),
        id="my-custom-evaluator",
        type=LLMObsCustomEvalConfigType.EVALUATOR_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_custom_eval_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.update_llm_obs_custom_eval_config(eval_name="eval_name", body=body)
