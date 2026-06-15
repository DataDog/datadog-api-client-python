"""
Trigger a patterns run returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_patterns_request_type import LLMObsPatternsRequestType
from datadog_api_client.v2.model.llm_obs_patterns_trigger_request import LLMObsPatternsTriggerRequest
from datadog_api_client.v2.model.llm_obs_patterns_trigger_request_attributes import (
    LLMObsPatternsTriggerRequestAttributes,
)
from datadog_api_client.v2.model.llm_obs_patterns_trigger_request_data import LLMObsPatternsTriggerRequestData

body = LLMObsPatternsTriggerRequest(
    data=LLMObsPatternsTriggerRequestData(
        attributes=LLMObsPatternsTriggerRequestAttributes(
            config_id="a7c8d9e0-1234-5678-9abc-def012345678",
        ),
        type=LLMObsPatternsRequestType.TOPIC_DISCOVERY,
    ),
)

configuration = Configuration()
configuration.unstable_operations["trigger_llm_obs_patterns"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.trigger_llm_obs_patterns(body=body)

    print(response)
