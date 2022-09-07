"""
Restore deleted dashboards returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard_bulk_action_data import DashboardBulkActionData
from datadog_api_client.v1.model.dashboard_bulk_action_data_list import DashboardBulkActionDataList
from datadog_api_client.v1.model.dashboard_resource_type import DashboardResourceType
from datadog_api_client.v1.model.dashboard_restore_request import DashboardRestoreRequest

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

body = DashboardRestoreRequest(
    data=DashboardBulkActionDataList(
        [
            DashboardBulkActionData(
                id=DASHBOARD_ID,
                type=DashboardResourceType.DASHBOARD,
            ),
        ]
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    api_instance.restore_dashboards(body=body)
