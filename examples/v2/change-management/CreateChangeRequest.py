"""
Create a change request returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.change_management_api import ChangeManagementApi
from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType
from datadog_api_client.v2.model.change_request_create_attributes import ChangeRequestCreateAttributes
from datadog_api_client.v2.model.change_request_create_data import ChangeRequestCreateData
from datadog_api_client.v2.model.change_request_create_request import ChangeRequestCreateRequest
from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType
from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
from datetime import datetime
from dateutil.tz import tzutc

body = ChangeRequestCreateRequest(
    data=ChangeRequestCreateData(
        attributes=ChangeRequestCreateAttributes(
            change_request_linked_incident_uuid="00000000-0000-0000-0000-000000000000",
            change_request_maintenance_window_query="",
            change_request_plan="1. Deploy to staging 2. Run tests 3. Deploy to production",
            change_request_risk=ChangeRequestRiskLevel.LOW,
            change_request_type=ChangeRequestChangeType.NORMAL,
            description="Deploying new payment service v2.1",
            end_date=datetime(2024, 1, 2, 15, 0, tzinfo=tzutc()),
            project_id="d4bbe1af-f36e-42f1-87c1-493ca35c320e",
            requested_teams=[
                "team-handle-1",
            ],
            start_date=datetime(2024, 1, 1, 3, 0, tzinfo=tzutc()),
            title="Deploy new payment service",
        ),
        type=ChangeRequestResourceType.CHANGE_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_change_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChangeManagementApi(api_client)
    response = api_instance.create_change_request(body=body)

    print(response)
