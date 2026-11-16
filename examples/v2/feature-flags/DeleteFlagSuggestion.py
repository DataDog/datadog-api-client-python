"""
Delete or discard a flag change suggestion returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    api_instance.delete_flag_suggestion(
        suggestion_id=UUID("550e8400-e29b-41d4-a716-446655440020"),
    )
