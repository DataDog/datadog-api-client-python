"""
Update Scanning Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_group import SensitiveDataScannerGroup
from datadog_api_client.v2.model.sensitive_data_scanner_group_data import SensitiveDataScannerGroupData
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_rule_attributes import SensitiveDataScannerRuleAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_rule_relationships import SensitiveDataScannerRuleRelationships
from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType
from datadog_api_client.v2.model.sensitive_data_scanner_rule_update import SensitiveDataScannerRuleUpdate
from datadog_api_client.v2.model.sensitive_data_scanner_rule_update_request import SensitiveDataScannerRuleUpdateRequest
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement_type import (
    SensitiveDataScannerTextReplacementType,
)

# the "scanning_group" has a "scanning_rule"
RULE_DATA_ID = environ["RULE_DATA_ID"]

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

body = SensitiveDataScannerRuleUpdateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerRuleUpdate(
        id=RULE_DATA_ID,
        type=SensitiveDataScannerRuleType.SENSITIVE_DATA_SCANNER_RULE,
        attributes=SensitiveDataScannerRuleAttributes(
            name="Example-Update_Scanning_Rule_returns_OK_response",
            pattern="pattern",
            text_replacement=SensitiveDataScannerTextReplacement(
                type=SensitiveDataScannerTextReplacementType.NONE,
            ),
            tags=[
                "sensitive_data:true",
            ],
            is_enabled=True,
        ),
        relationships=SensitiveDataScannerRuleRelationships(
            group=SensitiveDataScannerGroupData(
                data=SensitiveDataScannerGroup(
                    type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
                    id=GROUP_DATA_ID,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.update_scanning_rule(rule_id=RULE_DATA_ID, body=body)

    print(response)
