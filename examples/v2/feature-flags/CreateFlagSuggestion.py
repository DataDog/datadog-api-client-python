"""
Create a flag suggestion returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.create_flag_suggestion_attributes import CreateFlagSuggestionAttributes
from datadog_api_client.v2.model.create_flag_suggestion_data import CreateFlagSuggestionData
from datadog_api_client.v2.model.create_flag_suggestion_request import CreateFlagSuggestionRequest
from datadog_api_client.v2.model.flag_suggestion_action import FlagSuggestionAction
from datadog_api_client.v2.model.flag_suggestion_data_type import FlagSuggestionDataType
from datadog_api_client.v2.model.flag_suggestion_property import FlagSuggestionProperty
from datadog_api_client.v2.model.suggestion_metadata import SuggestionMetadata
from uuid import UUID

body = CreateFlagSuggestionRequest(
    data=CreateFlagSuggestionData(
        attributes=CreateFlagSuggestionAttributes(
            action=FlagSuggestionAction.ARCHIVED,
            comment="Archive this deprecated flag",
            environment_id=UUID("550e8400-e29b-41d4-a716-446655440001"),
            notification_rule_targets=[
                "user@example.com",
            ],
            _property=FlagSuggestionProperty.FLAG,
            suggestion="ENABLED",
            suggestion_metadata=SuggestionMetadata(
                variant_id="550e8400-e29b-41d4-a716-446655440005",
            ),
        ),
        type=FlagSuggestionDataType.FLAG_SUGGESTIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_flag_suggestion(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"), body=body
    )

    print(response)
