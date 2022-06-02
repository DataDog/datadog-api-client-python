"""
Enable an AWS Logs integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi
from datadog_api_client.v1.model.aws_logs_services_request import AWSLogsServicesRequest

body = AWSLogsServicesRequest(
    account_id="1234567",
    services=[
        "s3",
        "elb",
        "elbv2",
        "cloudfront",
        "redshift",
        "lambda",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.enable_aws_log_services(body=body)

    print(response)
