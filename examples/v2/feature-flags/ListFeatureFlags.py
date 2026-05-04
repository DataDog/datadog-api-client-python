"""
List feature flags returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.list_feature_flags(
        limit=10,
    )

    print(response)
