"""
Update a shared dashboard returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard_global_time_live_span import DashboardGlobalTimeLiveSpan
from datadog_api_client.v1.model.dashboard_share_type import DashboardShareType
from datadog_api_client.v1.model.shared_dashboard_update_request import SharedDashboardUpdateRequest
from datadog_api_client.v1.model.shared_dashboard_update_request_global_time import (
    SharedDashboardUpdateRequestGlobalTime,
)

# there is a valid "shared_dashboard" in the system
SHARED_DASHBOARD_TOKEN = environ["SHARED_DASHBOARD_TOKEN"]

body = SharedDashboardUpdateRequest(
    global_time=SharedDashboardUpdateRequestGlobalTime(
        live_span=DashboardGlobalTimeLiveSpan.PAST_FIFTEEN_MINUTES,
    ),
    share_list=[],
    share_type=DashboardShareType.OPEN,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.update_public_dashboard(token=SHARED_DASHBOARD_TOKEN, body=body)

    print(response)
