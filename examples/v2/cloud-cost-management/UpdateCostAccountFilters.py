"""
Update account filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig
from datadog_api_client.v2.model.account_filters_patch_data import AccountFiltersPatchData
from datadog_api_client.v2.model.account_filters_patch_request import AccountFiltersPatchRequest
from datadog_api_client.v2.model.account_filters_patch_request_attributes import AccountFiltersPatchRequestAttributes
from datadog_api_client.v2.model.account_filters_patch_request_type import AccountFiltersPatchRequestType

body = AccountFiltersPatchRequest(
    data=AccountFiltersPatchData(
        attributes=AccountFiltersPatchRequestAttributes(
            account_filters=AccountFilteringConfig(
                excluded_accounts=[
                    "123456789123",
                    "123456789143",
                ],
                include_new_accounts=True,
                included_accounts=[
                    "123456789123",
                    "123456789143",
                ],
            ),
        ),
        type=AccountFiltersPatchRequestType.ACCOUNT_FILTERS_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_account_filters(cloud_account_id=9223372036854775807, body=body)

    print(response)
