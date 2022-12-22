"""
Delete Scanning Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_delete_request import SensitiveDataScannerRuleDeleteRequest

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = environ["RULE_DATA_ID"]

body = SensitiveDataScannerRuleDeleteRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.delete_scanning_rule(rule_id=RULE_DATA_ID, body=body)

    print(response)
