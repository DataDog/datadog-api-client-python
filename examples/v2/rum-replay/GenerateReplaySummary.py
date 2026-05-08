"""
Generate replay summary returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_replay_api import RumReplayApi
from datadog_api_client.v2.model.replay_summary_data_request import ReplaySummaryDataRequest
from datadog_api_client.v2.model.replay_summary_request import ReplaySummaryRequest
from datadog_api_client.v2.model.replay_summary_request_type import ReplaySummaryRequestType

body = ReplaySummaryRequest(
    data=ReplaySummaryDataRequest(
        type=ReplaySummaryRequestType.REPLAY_SUMMARY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["generate_replay_summary"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumReplayApi(api_client)
    response = api_instance.generate_replay_summary(
        session_id="00000000-0000-0000-0000-000000000001", data_source="rum", body=body
    )

    print(response)
