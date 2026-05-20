"""
Search LLM Observability experimentation entities returns "Partial Content — more results are available. Use
`meta.after` as the next `page.cursor`." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_experimentation_content_preview import LLMObsExperimentationContentPreview
from datadog_api_client.v2.model.llm_obs_experimentation_cursor_page import LLMObsExperimentationCursorPage
from datadog_api_client.v2.model.llm_obs_experimentation_filter import LLMObsExperimentationFilter
from datadog_api_client.v2.model.llm_obs_experimentation_include import LLMObsExperimentationInclude
from datadog_api_client.v2.model.llm_obs_experimentation_search_data_attributes_request import (
    LLMObsExperimentationSearchDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_search_data_request import (
    LLMObsExperimentationSearchDataRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_search_request import LLMObsExperimentationSearchRequest
from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType

body = LLMObsExperimentationSearchRequest(
    data=LLMObsExperimentationSearchDataRequest(
        attributes=LLMObsExperimentationSearchDataAttributesRequest(
            content_preview=LLMObsExperimentationContentPreview(
                limit=500,
            ),
            filter=LLMObsExperimentationFilter(
                include_deleted=False,
                is_deleted=False,
                query="my experiment",
                scope=[
                    "experiments",
                ],
                version=None,
            ),
            include=LLMObsExperimentationInclude(
                user_data=False,
            ),
            page=LLMObsExperimentationCursorPage(
                limit=100,
            ),
        ),
        type=LLMObsExperimentationType.EXPERIMENTATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["search_llm_obs_experimentation"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.search_llm_obs_experimentation(body=body)

    print(response)
