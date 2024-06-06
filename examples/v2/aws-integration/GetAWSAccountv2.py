"""
AWS Integration - Get account returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
configuration.unstable_operations["get_aws_accountv2"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_accountv2(
        aws_account_config_id="aws_account_config_id",
    )

    print(response)
