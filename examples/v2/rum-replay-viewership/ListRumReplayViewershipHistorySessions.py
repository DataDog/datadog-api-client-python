"""
List RUM replay viewership history sessions returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    response = api_instance.list_rum_replay_viewership_history_sessions()

    print(response)
