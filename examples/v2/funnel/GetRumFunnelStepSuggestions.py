"""
Get rum funnel step suggestions returns "Successful response with funnel step suggestions" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.funnel_api import FunnelApi
from datadog_api_client.v2.model.funnel_suggestion_request import FunnelSuggestionRequest
from datadog_api_client.v2.model.funnel_suggestion_request_data import FunnelSuggestionRequestData
from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes import FunnelSuggestionRequestDataAttributes
from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_search import (
    FunnelSuggestionRequestDataAttributesSearch,
)
from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_search_steps_items import (
    FunnelSuggestionRequestDataAttributesSearchStepsItems,
)
from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_term_search import (
    FunnelSuggestionRequestDataAttributesTermSearch,
)
from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_time import (
    FunnelSuggestionRequestDataAttributesTime,
)
from datadog_api_client.v2.model.funnel_suggestion_request_data_type import FunnelSuggestionRequestDataType

body = FunnelSuggestionRequest(
    data=FunnelSuggestionRequestData(
        attributes=FunnelSuggestionRequestDataAttributes(
            data_source="",
            search=FunnelSuggestionRequestDataAttributesSearch(
                cross_session_filter="",
                query_string="@type:view",
                steps=[
                    FunnelSuggestionRequestDataAttributesSearchStepsItems(
                        facet="@view.name",
                        step_filter="",
                        value="/apm/home",
                    ),
                ],
                subquery_id="",
            ),
            term_search=FunnelSuggestionRequestDataAttributesTermSearch(
                query="apm",
            ),
            time=FunnelSuggestionRequestDataAttributesTime(
                _from=1756425600000,
                to=1756857600000,
            ),
        ),
        id="funnel_suggestion_request",
        type=FunnelSuggestionRequestDataType.FUNNEL_SUGGESTION_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_rum_funnel_step_suggestions"] = True
with ApiClient(configuration) as api_client:
    api_instance = FunnelApi(api_client)
    response = api_instance.get_rum_funnel_step_suggestions(body=body)

    print(response)
