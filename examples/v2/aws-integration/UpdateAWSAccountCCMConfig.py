"""
Update AWS CCM config returns "AWS CCM Config object" response
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
                        bucket_name="billing-updated",
                        bucket_region="us-west-2",
                        report_name="cost-report-updated",
                        report_prefix="reports-updated",
                        report_type="CUR2.0",
                    ),
                ],
            ),
        ),
        type=AWSCcmConfigType.CCM_CONFIG,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.update_aws_account_ccm_config(
        aws_account_config_id="873c7e78-8915-4c7a-a3a7-33a57adf54f4", body=body
    )

    print(response)
