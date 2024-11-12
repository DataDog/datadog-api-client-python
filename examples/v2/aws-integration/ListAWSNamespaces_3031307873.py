"""
List namespaces returns "AWS Namespaces List object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_aws_namespaces"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.list_aws_namespaces()

    print(response)
