"""
Update a feature flag returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.update_feature_flag_attributes import UpdateFeatureFlagAttributes
from datadog_api_client.v2.model.update_feature_flag_data import UpdateFeatureFlagData
from datadog_api_client.v2.model.update_feature_flag_data_type import UpdateFeatureFlagDataType
from datadog_api_client.v2.model.update_feature_flag_request import UpdateFeatureFlagRequest

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ID = environ["FEATURE_FLAG_DATA_ID"]

body = UpdateFeatureFlagRequest(
    data=UpdateFeatureFlagData(
        type=UpdateFeatureFlagDataType.FEATURE_FLAGS,
        attributes=UpdateFeatureFlagAttributes(
            description="Updated description for the feature flag",
            name="Updated Test Feature Flag Example-Feature-Flag",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_feature_flag(feature_flag_id=FEATURE_FLAG_DATA_ID, body=body)

    print(response)
