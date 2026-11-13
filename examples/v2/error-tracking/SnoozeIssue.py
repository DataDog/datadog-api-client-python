"""
Snooze an issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issue_snooze_request import IssueSnoozeRequest
from datadog_api_client.v2.model.issue_snooze_request_data import IssueSnoozeRequestData
from datadog_api_client.v2.model.issue_snooze_request_data_attributes import IssueSnoozeRequestDataAttributes
from datadog_api_client.v2.model.issue_snooze_request_data_type import IssueSnoozeRequestDataType
from datadog_api_client.v2.model.issue_watch_condition import IssueWatchCondition
from datadog_api_client.v2.model.issue_watch_condition_kind import IssueWatchConditionKind

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

body = IssueSnoozeRequest(
    data=IssueSnoozeRequestData(
        attributes=IssueSnoozeRequestDataAttributes(
            condition=IssueWatchCondition(
                kind=IssueWatchConditionKind.ELAPSED_TIME,
                duration="168h",
            ),
        ),
        id=ISSUE_ID,
        type=IssueSnoozeRequestDataType.ERROR_TRACKING_ISSUE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["snooze_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.snooze_issue(issue_id=ISSUE_ID, body=body)

    print(response)
