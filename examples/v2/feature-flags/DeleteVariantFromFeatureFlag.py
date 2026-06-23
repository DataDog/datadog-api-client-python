"""
Delete a variant returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    api_instance.delete_variant_from_feature_flag(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        variant_id=UUID("550e8400-e29b-41d4-a716-446655440002"),
    )
