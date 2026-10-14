"""
List feature flags filters permanent staleness using computed details
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.feature_flag_staleness_status import FeatureFlagStalenessStatus

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.list_feature_flags(
        tags=[
            "list-test:example-feature-flag",
        ],
        staleness_status=FeatureFlagStalenessStatus.PERMANENT,
    )

    print(response)
