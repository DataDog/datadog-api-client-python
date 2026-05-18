"""
Reject a flag suggestion returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.flag_suggestion_event_data_type import FlagSuggestionEventDataType
from datadog_api_client.v2.model.review_flag_suggestion_attributes import ReviewFlagSuggestionAttributes
from datadog_api_client.v2.model.review_flag_suggestion_data import ReviewFlagSuggestionData
from datadog_api_client.v2.model.review_flag_suggestion_request import ReviewFlagSuggestionRequest
from uuid import UUID

body = ReviewFlagSuggestionRequest(
    data=ReviewFlagSuggestionData(
        attributes=ReviewFlagSuggestionAttributes(
            comment="Looks good, approved!",
        ),
        type=FlagSuggestionEventDataType.FLAG_SUGGESTION_EVENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.reject_flag_suggestion(
        suggestion_id=UUID("550e8400-e29b-41d4-a716-446655440020"), body=body
    )

    print(response)
