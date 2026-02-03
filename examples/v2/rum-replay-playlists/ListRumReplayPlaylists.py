"""
List rum replay playlists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.list_rum_replay_playlists()

    print(response)
