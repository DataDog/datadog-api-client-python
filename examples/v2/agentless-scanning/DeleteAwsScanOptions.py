"""
Delete AWS Scan Options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.delete_aws_scan_options(
        account_id="account_id",
    )
