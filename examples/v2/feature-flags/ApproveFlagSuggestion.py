"""
Approve a flag change suggestion returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.approve_flag_suggestion_attributes import ApproveFlagSuggestionAttributes
from datadog_api_client.v2.model.approve_flag_suggestion_data import ApproveFlagSuggestionData
from datadog_api_client.v2.model.approve_flag_suggestion_request import ApproveFlagSuggestionRequest
from datadog_api_client.v2.model.review_flag_suggestion_data_type import ReviewFlagSuggestionDataType
from uuid import UUID

body = ApproveFlagSuggestionRequest(
    data=ApproveFlagSuggestionData(
        attributes=ApproveFlagSuggestionAttributes(
            apply=False,
            comment="Approved for rollout.",
        ),
        type=ReviewFlagSuggestionDataType.FLAG_SUGGESTION_EVENTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.approve_flag_suggestion(
        suggestion_id=UUID("550e8400-e29b-41d4-a716-446655440020"), body=body
    )

    print(response)
