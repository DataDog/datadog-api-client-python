"""
Create a flag change suggestion returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.create_flag_suggestion_attributes import CreateFlagSuggestionAttributes
from datadog_api_client.v2.model.create_flag_suggestion_data import CreateFlagSuggestionData
from datadog_api_client.v2.model.create_flag_suggestion_request import CreateFlagSuggestionRequest
from datadog_api_client.v2.model.feature_flag_suggestion_data_type import FeatureFlagSuggestionDataType
from datadog_api_client.v2.model.feature_flag_suggestion_metadata_request import FeatureFlagSuggestionMetadataRequest
from uuid import UUID

body = CreateFlagSuggestionRequest(
    data=CreateFlagSuggestionData(
        attributes=CreateFlagSuggestionAttributes(
            action="updated",
            comment="Restrict this flag to server applications.",
            environment_id=UUID("550e8400-e29b-41d4-a716-446655440001"),
            notification_rule_targets=[
                "requester@example.com",
            ],
            _property="DISTRIBUTION_CHANNEL",
            suggestion="SERVER",
            suggestion_metadata=FeatureFlagSuggestionMetadataRequest(
                variant_id=UUID("550e8400-e29b-41d4-a716-446655440002"),
            ),
        ),
        type=FeatureFlagSuggestionDataType.FLAG_SUGGESTIONS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_flag_suggestion(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"), body=body
    )

    print(response)
