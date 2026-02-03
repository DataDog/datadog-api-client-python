"""
Create replay heatmap snapshot returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi
from datadog_api_client.v2.model.snapshot_create_request import SnapshotCreateRequest
from datadog_api_client.v2.model.snapshot_create_request_data import SnapshotCreateRequestData
from datadog_api_client.v2.model.snapshot_create_request_data_attributes import SnapshotCreateRequestDataAttributes
from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType

body = SnapshotCreateRequest(
    data=SnapshotCreateRequestData(
        attributes=SnapshotCreateRequestDataAttributes(
            application_id="aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb",
            device_type="desktop",
            event_id="11111111-2222-3333-4444-555555555555",
            is_device_type_selected_by_user=False,
            snapshot_name="My Snapshot",
            start=0,
            view_name="/home",
        ),
        type=SnapshotUpdateRequestDataType.SNAPSHOTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    response = api_instance.create_replay_heatmap_snapshot(body=body)

    print(response)
