"""
Create rum replay session watch returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_viewership_api import RumReplayViewershipApi
from datadog_api_client.v2.model.watch import Watch
from datadog_api_client.v2.model.watch_data import WatchData
from datadog_api_client.v2.model.watch_data_attributes import WatchDataAttributes
from datadog_api_client.v2.model.watch_data_type import WatchDataType
from datetime import datetime
from dateutil.tz import tzutc

body = Watch(
    data=WatchData(
        attributes=WatchDataAttributes(
            application_id="aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            event_id="11111111-2222-3333-4444-555555555555",
            timestamp=datetime(2026, 1, 13, 17, 15, 53, 208340, tzinfo=tzutc()),
        ),
        type=WatchDataType.RUM_REPLAY_WATCH,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayViewershipApi(api_client)
    response = api_instance.create_rum_replay_session_watch(
        session_id="00000000-0000-0000-0000-000000000001", body=body
    )

    print(response)
