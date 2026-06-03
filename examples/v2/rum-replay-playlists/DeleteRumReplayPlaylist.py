"""
Delete rum replay playlist returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    api_instance.delete_rum_replay_playlist(
        playlist_id=1234567,
    )
