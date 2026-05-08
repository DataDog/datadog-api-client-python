"""
List replay analysis issues returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_analysis_api import RumReplayAnalysisApi

configuration = Configuration()
configuration.unstable_operations["list_replay_analysis_issues"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumReplayAnalysisApi(api_client)
    response = api_instance.list_replay_analysis_issues()

    print(response)
