"""
Get AWS metric name filter preview returns "AWS metric name filter preview result" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_aws_metric_name_filter_preview"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_metric_name_filter_preview(
        aws_account_config_id="aws_account_config_id",
    )

    print(response)
