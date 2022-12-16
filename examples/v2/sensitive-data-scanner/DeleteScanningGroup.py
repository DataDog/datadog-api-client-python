"""
Delete Scanning Group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_group_delete_request import (
    SensitiveDataScannerGroupDeleteRequest,
)
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

body = SensitiveDataScannerGroupDeleteRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.delete_scanning_group(group_id=GROUP_DATA_ID, body=body)

    print(response)
