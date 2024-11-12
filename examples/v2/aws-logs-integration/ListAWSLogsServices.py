"""
Get list of AWS log ready services returns "AWS Logs Services List object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_logs_integration_api import AWSLogsIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_aws_logs_services"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSLogsIntegrationApi(api_client)
    response = api_instance.list_aws_logs_services()

    print(response)
