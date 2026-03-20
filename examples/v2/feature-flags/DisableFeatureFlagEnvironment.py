"""
Disable a feature flag in an environment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ID = environ["FEATURE_FLAG_DATA_ID"]

# there is a valid "environment" in the system
ENVIRONMENT_DATA_ID = environ["ENVIRONMENT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    api_instance.disable_feature_flag_environment(
        feature_flag_id=FEATURE_FLAG_DATA_ID,
        environment_id=ENVIRONMENT_DATA_ID,
    )
