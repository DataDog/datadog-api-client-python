"""
Bulk remove rum replay playlist sessions returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_playlists_api import RumReplayPlaylistsApi
from datadog_api_client.v2.model.session_id_array import SessionIdArray
from datadog_api_client.v2.model.session_id_data import SessionIdData
from datadog_api_client.v2.model.viewership_history_session_data_type import ViewershipHistorySessionDataType

body = SessionIdArray(
    data=[
        SessionIdData(
            id="00000000-0000-0000-0000-000000000001",
            type=ViewershipHistorySessionDataType.RUM_REPLAY_SESSION,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayPlaylistsApi(api_client)
    api_instance.bulk_remove_rum_replay_playlist_sessions(playlist_id=1234567, body=body)
