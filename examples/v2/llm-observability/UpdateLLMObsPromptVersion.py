"""
Update a specific LLM Observability prompt version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_prompt_version_type import LLMObsPromptVersionType
from datadog_api_client.v2.model.llm_obs_update_prompt_version_data import LLMObsUpdatePromptVersionData
from datadog_api_client.v2.model.llm_obs_update_prompt_version_data_attributes import (
    LLMObsUpdatePromptVersionDataAttributes,
)
from datadog_api_client.v2.model.llm_obs_update_prompt_version_request import LLMObsUpdatePromptVersionRequest

# there is a valid "prompt" in the system
PROMPT_DATA_ATTRIBUTES_PROMPT_ID = environ["PROMPT_DATA_ATTRIBUTES_PROMPT_ID"]

# there is a valid "prompt_version" in the system
PROMPT_VERSION_DATA_ATTRIBUTES_VERSION = environ["PROMPT_VERSION_DATA_ATTRIBUTES_VERSION"]

body = LLMObsUpdatePromptVersionRequest(
    data=LLMObsUpdatePromptVersionData(
        attributes=LLMObsUpdatePromptVersionDataAttributes(
            description="Give concise answers and cite relevant help-center articles.",
        ),
        type=LLMObsPromptVersionType.PROMPT_TEMPLATE_VERSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_prompt_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_prompt_version(
        prompt_id=PROMPT_DATA_ATTRIBUTES_PROMPT_ID, version=int(PROMPT_VERSION_DATA_ATTRIBUTES_VERSION), body=body
    )

    print(response)
