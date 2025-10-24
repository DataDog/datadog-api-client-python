"""
Update Azure scan options returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.azure_scan_options_input_update import AzureScanOptionsInputUpdate
from datadog_api_client.v2.model.azure_scan_options_input_update_data import AzureScanOptionsInputUpdateData
from datadog_api_client.v2.model.azure_scan_options_input_update_data_type import AzureScanOptionsInputUpdateDataType

body = AzureScanOptionsInputUpdate(
    data=AzureScanOptionsInputUpdateData(
        id="12345678-90ab-cdef-1234-567890abcdef",
        type=AzureScanOptionsInputUpdateDataType.AZURE_SCAN_OPTIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.update_azure_scan_options(subscription_id="12345678-90ab-cdef-1234-567890abcdef", body=body)

    print(response)
