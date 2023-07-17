"""
Send shared dashboard invitation email returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard_invite_type import DashboardInviteType
from datadog_api_client.v1.model.shared_dashboard_invites import SharedDashboardInvites
from datadog_api_client.v1.model.shared_dashboard_invites_data_object import SharedDashboardInvitesDataObject
from datadog_api_client.v1.model.shared_dashboard_invites_data_object_attributes import (
    SharedDashboardInvitesDataObjectAttributes,
)

# there is a valid "shared_dashboard" in the system
SHARED_DASHBOARD_TOKEN = environ["SHARED_DASHBOARD_TOKEN"]

body = SharedDashboardInvites(
    data=SharedDashboardInvitesDataObject(
        attributes=SharedDashboardInvitesDataObjectAttributes(
            email="exampledashboard@datadoghq.com",
        ),
        type=DashboardInviteType.PUBLIC_DASHBOARD_INVITATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.send_public_dashboard_invitation(token=SHARED_DASHBOARD_TOKEN, body=body)

    print(response)
