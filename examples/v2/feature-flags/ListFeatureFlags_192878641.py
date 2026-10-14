"""
List feature flags gives page parameters precedence over aliases
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.list_feature_flags(
        limit=2,
        offset=1,
        tags=[
            "list-test:example-feature-flag",
        ],
        sort="name",
        page_limit=1,
        page_offset=0,
    )

    print(response)
