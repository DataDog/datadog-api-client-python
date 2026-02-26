"""
Create AWS CCM config returns "AWS CCM Config object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_ccm_config import AWSCcmConfig
from datadog_api_client.v2.model.aws_ccm_config_request import AWSCcmConfigRequest
from datadog_api_client.v2.model.aws_ccm_config_request_attributes import AWSCcmConfigRequestAttributes
from datadog_api_client.v2.model.aws_ccm_config_request_data import AWSCcmConfigRequestData
from datadog_api_client.v2.model.aws_ccm_config_type import AWSCcmConfigType
from datadog_api_client.v2.model.data_export_config import DataExportConfig

body = AWSCcmConfigRequest(
    data=AWSCcmConfigRequestData(
        attributes=AWSCcmConfigRequestAttributes(
            ccm_config=AWSCcmConfig(
                data_export_configs=[
                    DataExportConfig(
                        bucket_name="billing",
                        bucket_region="us-east-1",
                        report_name="cost-and-usage-report",
                        report_prefix="reports",
                        report_type="CUR2.0",
                    ),
                ],
            ),
        ),
        type=AWSCcmConfigType.CCM_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_aws_account_ccm_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account_ccm_config(aws_account_config_id="aws_account_config_id", body=body)

    print(response)
