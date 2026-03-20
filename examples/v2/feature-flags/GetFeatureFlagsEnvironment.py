"""
Get an environment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi

# there is a valid "environment" in the system
ENVIRONMENT_DATA_ID = environ["ENVIRONMENT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.get_feature_flags_environment(
        environment_id=ENVIRONMENT_DATA_ID,
    )

    print(response)
