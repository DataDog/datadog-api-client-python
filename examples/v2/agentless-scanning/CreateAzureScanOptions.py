"""
Create Azure scan options returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.azure_scan_options import AzureScanOptions
from datadog_api_client.v2.model.azure_scan_options_data import AzureScanOptionsData
from datadog_api_client.v2.model.azure_scan_options_data_attributes import AzureScanOptionsDataAttributes
from datadog_api_client.v2.model.azure_scan_options_data_type import AzureScanOptionsDataType

body = AzureScanOptions(
    data=AzureScanOptionsData(
        attributes=AzureScanOptionsDataAttributes(
            vuln_containers_os=True,
            vuln_host_os=True,
        ),
        id="12345678-90ab-cdef-1234-567890abcdef",
        type=AzureScanOptionsDataType.AZURE_SCAN_OPTIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_azure_scan_options(body=body)

    print(response)
