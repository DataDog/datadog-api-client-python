"""
Query accounts returns "Successful response with account data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.query_account_request import QueryAccountRequest
from datadog_api_client.v2.model.query_account_request_data import QueryAccountRequestData
from datadog_api_client.v2.model.query_account_request_data_attributes import QueryAccountRequestDataAttributes
from datadog_api_client.v2.model.query_account_request_data_attributes_sort import QueryAccountRequestDataAttributesSort
from datadog_api_client.v2.model.query_account_request_data_type import QueryAccountRequestDataType

body = QueryAccountRequest(
    data=QueryAccountRequestData(
        attributes=QueryAccountRequestDataAttributes(
            limit=20,
            query="plan_type:enterprise AND user_count:>100 AND subscription_status:active",
            select_columns=[
                "account_id",
                "account_name",
                "user_count",
                "plan_type",
                "subscription_status",
                "created_at",
                "mrr",
                "industry",
            ],
            sort=QueryAccountRequestDataAttributesSort(
                field="user_count",
                order="DESC",
            ),
            wildcard_search_term="tech",
        ),
        id="query_account_request",
        type=QueryAccountRequestDataType.QUERY_ACCOUNT_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["query_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.query_accounts(body=body)

    print(response)
