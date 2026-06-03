"""
Update rum replay playlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi
from datadog_api_client.v2.model.playlist import Playlist
from datadog_api_client.v2.model.playlist_data import PlaylistData
from datadog_api_client.v2.model.playlist_data_attributes import PlaylistDataAttributes
from datadog_api_client.v2.model.playlist_data_attributes_created_by import PlaylistDataAttributesCreatedBy
from datadog_api_client.v2.model.playlist_data_type import PlaylistDataType

body = Playlist(
    data=PlaylistData(
        attributes=PlaylistDataAttributes(
            created_by=PlaylistDataAttributesCreatedBy(
                handle="john.doe@example.com",
                id="00000000-0000-0000-0000-000000000001",
                uuid="00000000-0000-0000-0000-000000000001",
            ),
            name="My Playlist",
        ),
        type=PlaylistDataType.RUM_REPLAY_PLAYLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    response = api_instance.update_rum_replay_playlist(playlist_id=1234567, body=body)

    print(response)
