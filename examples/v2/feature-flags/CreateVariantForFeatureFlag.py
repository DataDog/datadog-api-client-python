"""
Add a variant to a feature flag returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.create_variant import CreateVariant
from uuid import UUID

body = CreateVariant(
    key="variant-abc123",
    name="Variant ABC123",
    value="true",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_variant_for_feature_flag(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"), body=body
    )

    print(response)
