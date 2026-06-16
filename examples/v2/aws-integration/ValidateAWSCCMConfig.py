"""
Validate AWS CCM config returns "AWS CCM Config validation result" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_ccm_config_validation_request import AWSCcmConfigValidationRequest
from datadog_api_client.v2.model.aws_ccm_config_validation_request_attributes import (
    AWSCcmConfigValidationRequestAttributes,
)
from datadog_api_client.v2.model.aws_ccm_config_validation_request_data import AWSCcmConfigValidationRequestData
from datadog_api_client.v2.model.aws_ccm_config_validation_type import AWSCcmConfigValidationType

body = AWSCcmConfigValidationRequest(
    data=AWSCcmConfigValidationRequestData(
        attributes=AWSCcmConfigValidationRequestAttributes(
            account_id="123456789012",
            bucket_name="billing",
            bucket_region="us-east-1",
            report_name="cost-and-usage-report",
            report_prefix="reports",
        ),
        type=AWSCcmConfigValidationType.CCM_CONFIG_VALIDATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["validate_awsccm_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.validate_awsccm_config(body=body)

    print(response)
