"""
Post AWS Scan Options returns "Agentless scan options enabled successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.aws_scan_options_create_attributes import AwsScanOptionsCreateAttributes
from datadog_api_client.v2.model.aws_scan_options_create_data import AwsScanOptionsCreateData
from datadog_api_client.v2.model.aws_scan_options_create_request import AwsScanOptionsCreateRequest
from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType

body = AwsScanOptionsCreateRequest(
    data=AwsScanOptionsCreateData(
        id="000000000003",
        type=AwsScanOptionsType.AWS_SCAN_OPTIONS,
        attributes=AwsScanOptionsCreateAttributes(
            _lambda=True,
            sensitive_data=False,
            vuln_containers_os=True,
            vuln_host_os=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_aws_scan_options(body=body)

    print(response)
