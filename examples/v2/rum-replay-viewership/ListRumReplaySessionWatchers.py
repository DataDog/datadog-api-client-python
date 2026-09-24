"""
List RUM replay session watchers returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    response = api_instance.list_rum_replay_session_watchers(
        session_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
