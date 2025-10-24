"""
Update GCP scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.gcp_scan_options_input_update import GcpScanOptionsInputUpdate
from datadog_api_client.v2.model.gcp_scan_options_input_update_data import GcpScanOptionsInputUpdateData
from datadog_api_client.v2.model.gcp_scan_options_input_update_data_attributes import (
    GcpScanOptionsInputUpdateDataAttributes,
)
from datadog_api_client.v2.model.gcp_scan_options_input_update_data_type import GcpScanOptionsInputUpdateDataType

body = GcpScanOptionsInputUpdate(
    data=GcpScanOptionsInputUpdateData(
        id="api-spec-test",
        type=GcpScanOptionsInputUpdateDataType.GCP_SCAN_OPTIONS,
        attributes=GcpScanOptionsInputUpdateDataAttributes(
            vuln_containers_os=False,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.update_gcp_scan_options(project_id="api-spec-test", body=body)

    print(response)
