"""
Create or update a patterns configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_patterns_config_type import LLMObsPatternsConfigType
from datadog_api_client.v2.model.llm_obs_patterns_config_upsert_request import LLMObsPatternsConfigUpsertRequest
from datadog_api_client.v2.model.llm_obs_patterns_config_upsert_request_attributes import (
    LLMObsPatternsConfigUpsertRequestAttributes,
)
from datadog_api_client.v2.model.llm_obs_patterns_config_upsert_request_data import (
    LLMObsPatternsConfigUpsertRequestData,
)

body = LLMObsPatternsConfigUpsertRequest(
    data=LLMObsPatternsConfigUpsertRequestData(
        attributes=LLMObsPatternsConfigUpsertRequestAttributes(
            account_id="1000000001",
            config_id="a7c8d9e0-1234-5678-9abc-def012345678",
            evp_query="@ml_app:support-bot",
            hierarchy_depth=2,
            integration_provider="openai",
            model_name="gpt-4o",
            name="Support chatbot topics",
            num_records=1000,
            sampling_ratio=0.1,
            scope="",
            template="",
        ),
        type=LLMObsPatternsConfigType.TOPIC_DISCOVERY_CONFIGS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_llm_obs_patterns_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.upsert_llm_obs_patterns_config(body=body)

    print(response)
