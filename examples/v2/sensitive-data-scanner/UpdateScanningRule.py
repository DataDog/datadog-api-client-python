"""
Update Scanning Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_included_keyword_configuration import (
    SensitiveDataScannerIncludedKeywordConfiguration,
)
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_attributes import SensitiveDataScannerRuleAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType
from datadog_api_client.v2.model.sensitive_data_scanner_rule_update import SensitiveDataScannerRuleUpdate
from datadog_api_client.v2.model.sensitive_data_scanner_rule_update_request import SensitiveDataScannerRuleUpdateRequest
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement_type import (
    SensitiveDataScannerTextReplacementType,
)

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = environ["RULE_DATA_ID"]

body = SensitiveDataScannerRuleUpdateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerRuleUpdate(
        id=RULE_DATA_ID,
        type=SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE,
        attributes=SensitiveDataScannerRuleAttributes(
            name="Example-Sensitive-Data-Scanner",
            pattern="pattern",
            text_replacement=SensitiveDataScannerTextReplacement(
                type=SensitiveDataScannerTextReplacementType.NONE,
            ),
            tags=[
                "sensitive_data:true",
            ],
            is_enabled=True,
            priority=5,
            included_keyword_configuration=SensitiveDataScannerIncludedKeywordConfiguration(
                keywords=[
                    "credit card",
                    "cc",
                ],
                character_count=35,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.update_scanning_rule(rule_id=RULE_DATA_ID, body=body)

    print(response)
