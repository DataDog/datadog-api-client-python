"""
Get AWS scan options returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

# there is a valid "aws_scan_options" in the system
AWS_SCAN_OPTIONS_ID = environ["AWS_SCAN_OPTIONS_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.get_aws_scan_options(
        account_id=AWS_SCAN_OPTIONS_ID,
    )

    print(response)
