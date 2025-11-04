"""
Query users returns "Successful response with user data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.query_users_request import QueryUsersRequest
from datadog_api_client.v2.model.query_users_request_data import QueryUsersRequestData
from datadog_api_client.v2.model.query_users_request_data_attributes import QueryUsersRequestDataAttributes
from datadog_api_client.v2.model.query_users_request_data_attributes_sort import QueryUsersRequestDataAttributesSort
from datadog_api_client.v2.model.query_users_request_data_type import QueryUsersRequestDataType

body = QueryUsersRequest(
    data=QueryUsersRequestData(
        attributes=QueryUsersRequestDataAttributes(
            limit=25,
            query="user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome",
            select_columns=[
                "user_id",
                "user_email",
                "user_name",
                "user_org_id",
                "first_country_code",
                "first_browser_name",
                "first_device_type",
                "last_seen",
            ],
            sort=QueryUsersRequestDataAttributesSort(
                field="first_seen",
                order="DESC",
            ),
            wildcard_search_term="john",
        ),
        id="query_users_request",
        type=QueryUsersRequestDataType.QUERY_USERS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.query_users(body=body)

    print(response)
