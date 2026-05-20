"""
Simple search experimentation entities returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_experimentation_content_preview import LLMObsExperimentationContentPreview
from datadog_api_client.v2.model.llm_obs_experimentation_filter import LLMObsExperimentationFilter
from datadog_api_client.v2.model.llm_obs_experimentation_include import LLMObsExperimentationInclude
from datadog_api_client.v2.model.llm_obs_experimentation_number_page import LLMObsExperimentationNumberPage
from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_attributes_request import (
    LLMObsExperimentationSimpleSearchDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_request import (
    LLMObsExperimentationSimpleSearchDataRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_request import (
    LLMObsExperimentationSimpleSearchRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_sort_field import LLMObsExperimentationSortField
from datadog_api_client.v2.model.llm_obs_experimentation_sort_field_direction import (
    LLMObsExperimentationSortFieldDirection,
)
from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType

body = LLMObsExperimentationSimpleSearchRequest(
    data=LLMObsExperimentationSimpleSearchDataRequest(
        attributes=LLMObsExperimentationSimpleSearchDataAttributesRequest(
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
            page=LLMObsExperimentationNumberPage(
                limit=50,
                number=1,
            ),
            sort=[
                LLMObsExperimentationSortField(
                    direction=LLMObsExperimentationSortFieldDirection.DESC,
                    field="created_at",
                ),
            ],
        ),
        type=LLMObsExperimentationType.EXPERIMENTATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["simple_search_llm_obs_experimentation"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.simple_search_llm_obs_experimentation(body=body)

    print(response)
