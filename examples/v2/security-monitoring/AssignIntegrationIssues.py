"""
Assign or un-assign Jira issues to security findings returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.integration_assignment_data_attributes_request import (
    IntegrationAssignmentDataAttributesRequest,
)
from datadog_api_client.v2.model.integration_assignment_data_attributes_request_action import (
    IntegrationAssignmentDataAttributesRequestAction,
)
from datadog_api_client.v2.model.integration_assignment_data_attributes_request_assignment import (
    IntegrationAssignmentDataAttributesRequestAssignment,
)
from datadog_api_client.v2.model.integration_assignment_data_attributes_request_type import (
    IntegrationAssignmentDataAttributesRequestType,
)
from datadog_api_client.v2.model.integration_assignment_data_request import IntegrationAssignmentDataRequest
from datadog_api_client.v2.model.integration_assignment_request import IntegrationAssignmentRequest
from datadog_api_client.v2.model.integration_assignment_type import IntegrationAssignmentType

body = IntegrationAssignmentRequest(
    data=IntegrationAssignmentDataRequest(
        attributes=IntegrationAssignmentDataAttributesRequest(
            action=IntegrationAssignmentDataAttributesRequestAction.ASSIGN,
            assignment=IntegrationAssignmentDataAttributesRequestAssignment(
                jira={
                    "https://jira.example.com/browse/SEC-123": [
                        "MDBjMzdhYzgyNGZkZGJiZmY0OGNmYjNiMWQ2ODY0YmR-OTc0YjMzNjM1Y2UyODA2YTEyNWQxYmNkZjhmODllNzg=",
                    ],
                },
            ),
            type=IntegrationAssignmentDataAttributesRequestType.FINDINGS,
        ),
        id="some_id",
        type=IntegrationAssignmentType.ISSUE_ASSIGNMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["assign_integration_issues"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.assign_integration_issues(body=body)
