"""
Delete replay heatmap snapshot returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    api_instance.delete_replay_heatmap_snapshot(
        snapshot_id="00000000-0000-0000-0000-000000000001",
    )
