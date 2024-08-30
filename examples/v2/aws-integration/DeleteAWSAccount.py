"""
AWS Integration - Delete account config returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID = environ["AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_aws_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    api_instance.delete_aws_account(
        aws_account_id=AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID,
    )
