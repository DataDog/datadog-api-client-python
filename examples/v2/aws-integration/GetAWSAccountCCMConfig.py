"""
Get AWS CCM config returns "AWS CCM Config object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
configuration.unstable_operations["get_aws_account_ccm_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_account_ccm_config(
        aws_account_config_id="aws_account_config_id",
    )

    print(response)
