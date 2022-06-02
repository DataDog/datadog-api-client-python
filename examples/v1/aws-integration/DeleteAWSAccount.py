"""
Delete an AWS integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_account_delete_request import AWSAccountDeleteRequest

body = AWSAccountDeleteRequest(
    account_id="1234567",
    role_name="DatadogAWSIntegrationRole",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_account(body=body)

    print(response)
