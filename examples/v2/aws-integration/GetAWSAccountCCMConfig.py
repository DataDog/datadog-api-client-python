"""
Get AWS CCM config returns "AWS CCM Config object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_account_ccm_config(
        aws_account_config_id="873c7e78-8915-4c7a-a3a7-33a57adf54f4",
    )

    print(response)
