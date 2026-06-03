"""
Submit libraries for vulnerability scanning returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.mcp_scan_request import McpScanRequest
from datadog_api_client.v2.model.mcp_scan_request_data import McpScanRequestData
from datadog_api_client.v2.model.mcp_scan_request_data_attributes import McpScanRequestDataAttributes
from datadog_api_client.v2.model.mcp_scan_request_data_attributes_libraries_items import (
    McpScanRequestDataAttributesLibrariesItems,
)
from datadog_api_client.v2.model.mcp_scan_request_data_type import McpScanRequestDataType

body = McpScanRequest(
    data=McpScanRequestData(
        attributes=McpScanRequestDataAttributes(
            commit_hash="0e9fc8de83eaabecd722e1cd0ed44fb489fe15fc",
            libraries=[
                McpScanRequestDataAttributesLibrariesItems(
                    exclusions=[],
                    is_dev=False,
                    is_direct=True,
                    package_manager="nuget",
                    purl="pkg:nuget/Newtonsoft.Json@13.0.1",
                    target_frameworks=[],
                ),
            ],
            resource_name="my-org/my-repo",
        ),
        type=McpScanRequestDataType.MCPSCANREQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_scan"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_sca_scan(body=body)

    print(response)
