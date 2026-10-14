"""
List feature flags filters disabled production status
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.feature_flag_production_status import FeatureFlagProductionStatus

# there is a valid "feature_flag_list_a" in the system
FEATURE_FLAG_LIST_A_DATA_ID = environ["FEATURE_FLAG_LIST_A_DATA_ID"]

# there is a valid "feature_flag_list_b" in the system
FEATURE_FLAG_LIST_B_DATA_ID = environ["FEATURE_FLAG_LIST_B_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.list_feature_flags(
        production_status=[
            FeatureFlagProductionStatus.DISABLED,
        ],
        flag_ids=[
            FEATURE_FLAG_LIST_A_DATA_ID,
            FEATURE_FLAG_LIST_B_DATA_ID,
        ],
    )

    print(response)
