"""
Query event filtered users returns "Successful response with filtered user data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.query_event_filtered_users_request import QueryEventFilteredUsersRequest
from datadog_api_client.v2.model.query_event_filtered_users_request_data import QueryEventFilteredUsersRequestData
from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes import (
    QueryEventFilteredUsersRequestDataAttributes,
)
from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query import (
    QueryEventFilteredUsersRequestDataAttributesEventQuery,
)
from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query_time_frame import (
    QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame,
)
from datadog_api_client.v2.model.query_event_filtered_users_request_data_type import (
    QueryEventFilteredUsersRequestDataType,
)

body = QueryEventFilteredUsersRequest(
    data=QueryEventFilteredUsersRequestData(
        attributes=QueryEventFilteredUsersRequestDataAttributes(
            event_query=QueryEventFilteredUsersRequestDataAttributesEventQuery(
                query="@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform",
                time_frame=QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame(
                    end=1761309676,
                    start=1760100076,
                ),
            ),
            include_row_count=True,
            limit=25,
            query="user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome",
            select_columns=[
                "user_id",
                "user_email",
                "first_country_code",
                "first_browser_name",
                "events_count",
                "session_count",
                "error_count",
                "avg_loading_time",
            ],
        ),
        id="query_event_filtered_users_request",
        type=QueryEventFilteredUsersRequestDataType.QUERY_EVENT_FILTERED_USERS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_event_filtered_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.query_event_filtered_users(body=body)

    print(response)
