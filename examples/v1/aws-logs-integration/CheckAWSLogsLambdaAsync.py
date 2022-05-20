"""
Check that an AWS Lambda Function exists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_account_and_lambda_request import AWSAccountAndLambdaRequest

body = AWSAccountAndLambdaRequest(
    account_id="1234567",
    lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.check_aws_logs_lambda_async(body=body)

    print(response)
