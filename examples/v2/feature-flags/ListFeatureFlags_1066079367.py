"""
List feature flags combines teams with legacy team tags
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.list_feature_flags(
        tags=[
            "list-test:example-feature-flag",
            "team:api-client-test-b",
        ],
        teams=[
            "api-client-test-a",
            "api-client-test-a",
        ],
    )

    print(response)
