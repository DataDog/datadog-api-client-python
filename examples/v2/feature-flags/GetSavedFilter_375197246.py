"""
Get a saved filter returns a saved list
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.get_saved_filter(
        saved_filter_id=UUID("fb44ff15-fe17-4bab-afe8-9a8eb0cf586c"),
    )

    print(response)
