"""
List standard patterns returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.list_standard_patterns()

    print(response)
