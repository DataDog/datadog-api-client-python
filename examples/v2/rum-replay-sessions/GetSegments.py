"""
Get segments returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_sessions_api import RumReplaySessionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumReplaySessionsApi(api_client)
    api_instance.get_segments(
        view_id="00000000-0000-0000-0000-000000000002",
        session_id="00000000-0000-0000-0000-000000000001",
    )
