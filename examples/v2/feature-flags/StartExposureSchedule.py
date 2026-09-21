"""
Start a progressive rollout returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.start_exposure_schedule(
        exposure_schedule_id=UUID("550e8400-e29b-41d4-a716-446655440010"),
    )

    print(response)
