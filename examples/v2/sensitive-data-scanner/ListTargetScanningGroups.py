"""
List Scanning Groups of a target returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_group_target import SensitiveDataScannerGroupTarget

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.list_target_scanning_groups(
        filter_target=SensitiveDataScannerGroupTarget.LLM_OBSERVABILITY,
    )

    print(response)
