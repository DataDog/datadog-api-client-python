"""
List replay heatmap snapshots returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_heatmaps_api import RumReplayHeatmapsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplayHeatmapsApi(api_client)
    response = api_instance.list_replay_heatmap_snapshots(
        filter_view_name="/home",
    )

    print(response)
