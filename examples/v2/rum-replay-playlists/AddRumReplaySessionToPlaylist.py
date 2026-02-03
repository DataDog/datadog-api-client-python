"""
Add rum replay session to playlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.add_rum_replay_session_to_playlist(
        ts=1704067200000,
        playlist_id=1234567,
        session_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
