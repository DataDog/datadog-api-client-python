"""
Create Cloud Cost Management AWS CUR config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.aws_cur_config_post_data import AwsCURConfigPostData
from datadog_api_client.v2.model.aws_cur_config_post_request import AwsCURConfigPostRequest
from datadog_api_client.v2.model.aws_cur_config_post_request_attributes import AwsCURConfigPostRequestAttributes
from datadog_api_client.v2.model.aws_cur_config_post_request_type import AwsCURConfigPostRequestType

body = AwsCURConfigPostRequest(
    data=AwsCURConfigPostData(
        attributes=AwsCURConfigPostRequestAttributes(
            account_id="123456789123",
            bucket_name="dd-cost-bucket",
            bucket_region="us-east-1",
            report_name="dd-report-name",
            report_prefix="dd-report-prefix",
        ),
        type=AwsCURConfigPostRequestType.AWS_CUR_CONFIG_POST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_awscur_config(body=body)

    print(response)
