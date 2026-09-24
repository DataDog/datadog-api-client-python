"""
Delete RUM replay session watch returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    api_instance.delete_rum_replay_session_watch(
        session_id="00000000-0000-0000-0000-000000000001",
    )
