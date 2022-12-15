"""
List Scanning Groups returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.list_scanning_groups()

    print(response)
