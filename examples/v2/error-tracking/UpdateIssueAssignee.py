"""
Update the assignee of an issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issue_update_assignee_request import IssueUpdateAssigneeRequest
from datadog_api_client.v2.model.issue_update_assignee_request_data import IssueUpdateAssigneeRequestData
from datadog_api_client.v2.model.issue_update_assignee_request_data_type import IssueUpdateAssigneeRequestDataType

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

body = IssueUpdateAssigneeRequest(
    data=IssueUpdateAssigneeRequestData(
        id="87cb11a0-278c-440a-99fe-701223c80296",
        type=IssueUpdateAssigneeRequestDataType.ASSIGNEE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.update_issue_assignee(issue_id=ISSUE_ID, body=body)

    print(response)
