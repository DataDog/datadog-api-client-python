"""
Update replay heatmap snapshot returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi
from datadog_api_client.v2.model.snapshot_update_request import SnapshotUpdateRequest
from datadog_api_client.v2.model.snapshot_update_request_data import SnapshotUpdateRequestData
from datadog_api_client.v2.model.snapshot_update_request_data_attributes import SnapshotUpdateRequestDataAttributes
from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType

body = SnapshotUpdateRequest(
    data=SnapshotUpdateRequestData(
        attributes=SnapshotUpdateRequestDataAttributes(
            event_id="11111111-2222-3333-4444-555555555555",
            is_device_type_selected_by_user=False,
            start=0,
        ),
        id="00000000-0000-0000-0000-000000000001",
        type=SnapshotUpdateRequestDataType.SNAPSHOTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    response = api_instance.update_replay_heatmap_snapshot(
        snapshot_id="00000000-0000-0000-0000-000000000001", body=body
    )

    print(response)
