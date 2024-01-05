"""
Update Cloud Cost Management AWS CUR config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.aws_cur_config_patch_data import AwsCURConfigPatchData
from datadog_api_client.v2.model.aws_cur_config_patch_request import AwsCURConfigPatchRequest
from datadog_api_client.v2.model.aws_cur_config_patch_request_attributes import AwsCURConfigPatchRequestAttributes
from datadog_api_client.v2.model.aws_cur_config_patch_request_type import AwsCURConfigPatchRequestType

body = AwsCURConfigPatchRequest(
    data=AwsCURConfigPatchData(
        attributes=AwsCURConfigPatchRequestAttributes(
            is_enabled=True,
        ),
        type=AwsCURConfigPatchRequestType.AWS_CUR_CONFIG_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_awscur_config(cloud_account_id="100", body=body)

    print(response)
