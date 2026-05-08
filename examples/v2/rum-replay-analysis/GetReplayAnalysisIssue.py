"""
Get replay analysis issue returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_analysis_api import RumReplayAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_replay_analysis_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumReplayAnalysisApi(api_client)
    response = api_instance.get_replay_analysis_issue(
        issue_id="00000000-0000-0000-0000-000000000001",
    )

    print(response)
