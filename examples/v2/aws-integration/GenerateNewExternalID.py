"""
AWS Integration - Generate new external ID returns "AWS External ID object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
configuration.unstable_operations["generate_new_external_id"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.generate_new_external_id()

    print(response)
