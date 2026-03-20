"""
Create a feature flag returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.create_feature_flag_attributes import CreateFeatureFlagAttributes
from datadog_api_client.v2.model.create_feature_flag_data import CreateFeatureFlagData
from datadog_api_client.v2.model.create_feature_flag_data_type import CreateFeatureFlagDataType
from datadog_api_client.v2.model.create_feature_flag_request import CreateFeatureFlagRequest
from datadog_api_client.v2.model.create_variant import CreateVariant
from datadog_api_client.v2.model.value_type import ValueType

body = CreateFeatureFlagRequest(
    data=CreateFeatureFlagData(
        type=CreateFeatureFlagDataType.FEATURE_FLAGS,
        attributes=CreateFeatureFlagAttributes(
            default_variant_key="variant-Example-Feature-Flag-1",
            description="Test feature flag for BDD scenarios",
            key="test-feature-flag-Example-Feature-Flag",
            name="Test Feature Flag Example-Feature-Flag",
            value_type=ValueType.BOOLEAN,
            variants=[
                CreateVariant(
                    key="variant-Example-Feature-Flag-1",
                    name="Variant Example-Feature-Flag A",
                    value="true",
                ),
                CreateVariant(
                    key="variant-Example-Feature-Flag-2",
                    name="Variant Example-Feature-Flag B",
                    value="false",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_feature_flag(body=body)

    print(response)
