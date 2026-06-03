"""
Remove rum replay session from playlist returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    api_instance.remove_rum_replay_session_from_playlist(
        playlist_id=1234567,
        session_id="00000000-0000-0000-0000-000000000001",
    )
