"""
Run an LLM inference returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_anthropic_effort import LLMObsAnthropicEffort
from datadog_api_client.v2.model.llm_obs_anthropic_metadata import LLMObsAnthropicMetadata
from datadog_api_client.v2.model.llm_obs_anthropic_thinking_config import LLMObsAnthropicThinkingConfig
from datadog_api_client.v2.model.llm_obs_anthropic_thinking_type import LLMObsAnthropicThinkingType
from datadog_api_client.v2.model.llm_obs_azure_open_ai_metadata import LLMObsAzureOpenAIMetadata
from datadog_api_client.v2.model.llm_obs_bedrock_metadata import LLMObsBedrockMetadata
from datadog_api_client.v2.model.llm_obs_inference_content import LLMObsInferenceContent
from datadog_api_client.v2.model.llm_obs_inference_content_value import LLMObsInferenceContentValue
from datadog_api_client.v2.model.llm_obs_inference_function import LLMObsInferenceFunction
from datadog_api_client.v2.model.llm_obs_inference_message import LLMObsInferenceMessage
from datadog_api_client.v2.model.llm_obs_inference_tool import LLMObsInferenceTool
from datadog_api_client.v2.model.llm_obs_inference_tool_call import LLMObsInferenceToolCall
from datadog_api_client.v2.model.llm_obs_inference_tool_result import LLMObsInferenceToolResult
from datadog_api_client.v2.model.llm_obs_integration_inference_request import LLMObsIntegrationInferenceRequest
from datadog_api_client.v2.model.llm_obs_integration_name import LLMObsIntegrationName
from datadog_api_client.v2.model.llm_obs_open_ai_metadata import LLMObsOpenAIMetadata
from datadog_api_client.v2.model.llm_obs_open_ai_reasoning_effort import LLMObsOpenAIReasoningEffort
from datadog_api_client.v2.model.llm_obs_open_ai_reasoning_summary import LLMObsOpenAIReasoningSummary
from datadog_api_client.v2.model.llm_obs_vertex_ai_metadata import LLMObsVertexAIMetadata

body = LLMObsIntegrationInferenceRequest(
    anthropic_metadata=LLMObsAnthropicMetadata(
        effort=LLMObsAnthropicEffort.MEDIUM,
        thinking=LLMObsAnthropicThinkingConfig(
            budget_tokens=1024,
            type=LLMObsAnthropicThinkingType.ENABLED,
        ),
    ),
    azure_openai_metadata=LLMObsAzureOpenAIMetadata(
        deployment_id="my-gpt4-deployment",
        model_version="0613",
        resource_name="my-azure-resource",
    ),
    bedrock_metadata=LLMObsBedrockMetadata(
        region="us-east-1",
    ),
    frequency_penalty=0.0,
    json_schema='{"type":"object","properties":{"answer":{"type":"string"}}}',
    max_completion_tokens=1024,
    max_tokens=1024,
    messages=[
        LLMObsInferenceMessage(
            content="What is the capital of France?",
            contents=[
                LLMObsInferenceContent(
                    type="text",
                    value=LLMObsInferenceContentValue(
                        text="Hello, how can I help you?",
                        tool_call=LLMObsInferenceToolCall(
                            arguments=dict([("location", "San Francisco")]),
                            name="get_weather",
                            tool_id="call_abc123",
                            type="function",
                        ),
                        tool_call_result=LLMObsInferenceToolResult(
                            name="get_weather",
                            result="The weather in San Francisco is 68°F and sunny.",
                            tool_id="call_abc123",
                            type="function",
                        ),
                    ),
                ),
            ],
            id="msg_001",
            role="user",
            tool_calls=[
                LLMObsInferenceToolCall(
                    arguments=dict([("location", "San Francisco")]),
                    name="get_weather",
                    tool_id="call_abc123",
                    type="function",
                ),
            ],
            tool_results=[
                LLMObsInferenceToolResult(
                    name="get_weather",
                    result="The weather in San Francisco is 68°F and sunny.",
                    tool_id="call_abc123",
                    type="function",
                ),
            ],
        ),
    ],
    model_id="gpt-4o",
    openai_metadata=LLMObsOpenAIMetadata(
        reasoning_effort=LLMObsOpenAIReasoningEffort.MEDIUM,
        reasoning_summary=LLMObsOpenAIReasoningSummary.AUTO,
    ),
    presence_penalty=0.0,
    temperature=0.7,
    tools=[
        LLMObsInferenceTool(
            function=LLMObsInferenceFunction(
                description="Get the current weather for a location.",
                name="get_weather",
                parameters=dict([("properties", "{'location': {'type': 'string'}}"), ("type", "object")]),
            ),
            type="function",
        ),
    ],
    top_k=50,
    top_p=1.0,
    vertex_ai_metadata=LLMObsVertexAIMetadata(
        location="us-central1",
        project="my-gcp-project",
        project_ids=[
            "my-gcp-project",
        ],
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_integration_inference"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_integration_inference(
        integration=LLMObsIntegrationName.OPENAI, account_id="account_id", body=body
    )

    print(response)
