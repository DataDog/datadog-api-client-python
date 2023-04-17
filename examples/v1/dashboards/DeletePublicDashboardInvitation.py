"""
Revoke shared dashboard invitations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard_invite_type import DashboardInviteType
from datadog_api_client.v1.model.shared_dashboard_invites import SharedDashboardInvites
from datadog_api_client.v1.model.shared_dashboard_invites_data_list import SharedDashboardInvitesDataList
from datadog_api_client.v1.model.shared_dashboard_invites_data_object import SharedDashboardInvitesDataObject
from datadog_api_client.v1.model.shared_dashboard_invites_data_object_attributes import (
    SharedDashboardInvitesDataObjectAttributes,
)

body = SharedDashboardInvites(
    data=SharedDashboardInvitesDataList(
        [
            SharedDashboardInvitesDataObject(
                attributes=SharedDashboardInvitesDataObjectAttributes(
                    email="test@datadoghq.com",
                ),
                type=DashboardInviteType.PUBLIC_DASHBOARD_INVITATION,
            ),
        ]
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    api_instance.delete_public_dashboard_invitation(token="token", body=body)
