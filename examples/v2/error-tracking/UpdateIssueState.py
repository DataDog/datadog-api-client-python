"""
Update the state of an issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issue_state import IssueState
from datadog_api_client.v2.model.issue_update_state_request import IssueUpdateStateRequest
from datadog_api_client.v2.model.issue_update_state_request_data import IssueUpdateStateRequestData
from datadog_api_client.v2.model.issue_update_state_request_data_attributes import IssueUpdateStateRequestDataAttributes
from datadog_api_client.v2.model.issue_update_state_request_data_type import IssueUpdateStateRequestDataType

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

body = IssueUpdateStateRequest(
    data=IssueUpdateStateRequestData(
        attributes=IssueUpdateStateRequestDataAttributes(
            state=IssueState.RESOLVED,
        ),
        id=ISSUE_ID,
        type=IssueUpdateStateRequestDataType.ERROR_TRACKING_ISSUE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.update_issue_state(issue_id=ISSUE_ID, body=body)

    print(response)
