"""
Archive a feature flag returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ID = environ["FEATURE_FLAG_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.archive_feature_flag(
        feature_flag_id=FEATURE_FLAG_DATA_ID,
    )

    print(response)
