"""
Update a variant returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.update_variant_attributes import UpdateVariantAttributes
from datadog_api_client.v2.model.update_variant_data import UpdateVariantData
from datadog_api_client.v2.model.update_variant_request import UpdateVariantRequest
from datadog_api_client.v2.model.variant_data_type import VariantDataType
from uuid import UUID

body = UpdateVariantRequest(
    data=UpdateVariantData(
        attributes=UpdateVariantAttributes(
            name="Variant ABC123 Updated",
            value="new_value",
        ),
        id=UUID("550e8400-e29b-41d4-a716-446655440002"),
        type=VariantDataType.VARIANTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    api_instance.update_variant_for_feature_flag(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        variant_id=UUID("550e8400-e29b-41d4-a716-446655440002"),
        body=body,
    )
