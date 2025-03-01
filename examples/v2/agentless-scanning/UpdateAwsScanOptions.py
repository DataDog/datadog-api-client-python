"""
Patch AWS Scan Options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType
from datadog_api_client.v2.model.aws_scan_options_update_attributes import AwsScanOptionsUpdateAttributes
from datadog_api_client.v2.model.aws_scan_options_update_data import AwsScanOptionsUpdateData
from datadog_api_client.v2.model.aws_scan_options_update_request import AwsScanOptionsUpdateRequest

body = AwsScanOptionsUpdateRequest(
    data=AwsScanOptionsUpdateData(
        type=AwsScanOptionsType.AWS_SCAN_OPTIONS,
        id="000000000002",
        attributes=AwsScanOptionsUpdateAttributes(
            vuln_host_os=True,
            vuln_containers_os=True,
            _lambda=False,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.update_aws_scan_options(account_id="000000000002", body=body)
