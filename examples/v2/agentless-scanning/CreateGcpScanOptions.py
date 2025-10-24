"""
Create GCP scan options returns "Agentless scan options enabled successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.gcp_scan_options import GcpScanOptions
from datadog_api_client.v2.model.gcp_scan_options_data import GcpScanOptionsData
from datadog_api_client.v2.model.gcp_scan_options_data_attributes import GcpScanOptionsDataAttributes
from datadog_api_client.v2.model.gcp_scan_options_data_type import GcpScanOptionsDataType

body = GcpScanOptions(
    data=GcpScanOptionsData(
        id="new-project",
        type=GcpScanOptionsDataType.GCP_SCAN_OPTIONS,
        attributes=GcpScanOptionsDataAttributes(
            vuln_host_os=True,
            vuln_containers_os=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_gcp_scan_options(body=body)

    print(response)
