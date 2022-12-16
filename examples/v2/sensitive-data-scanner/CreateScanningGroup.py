"""
Create Scanning Group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_configuration import SensitiveDataScannerConfiguration
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_data import SensitiveDataScannerConfigurationData
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import SensitiveDataScannerConfigurationType
from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
from datadog_api_client.v2.model.sensitive_data_scanner_group_attributes import SensitiveDataScannerGroupAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_group_create import SensitiveDataScannerGroupCreate
from datadog_api_client.v2.model.sensitive_data_scanner_group_create_request import (
    SensitiveDataScannerGroupCreateRequest,
)
from datadog_api_client.v2.model.sensitive_data_scanner_group_relationships import (
    SensitiveDataScannerGroupRelationships,
)
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct
from datadog_api_client.v2.model.sensitive_data_scanner_rule_data import SensitiveDataScannerRuleData

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = environ["CONFIGURATION_DATA_ID"]

body = SensitiveDataScannerGroupCreateRequest(
    meta=SensitiveDataScannerMetaVersionOnly(),
    data=SensitiveDataScannerGroupCreate(
        type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
        attributes=SensitiveDataScannerGroupAttributes(
            name="Example-Create_Scanning_Group_returns_OK_response",
            is_enabled=False,
            product_list=[
                SensitiveDataScannerProduct.LOGS,
            ],
            filter=SensitiveDataScannerFilter(
                query="*",
            ),
        ),
        relationships=SensitiveDataScannerGroupRelationships(
            configuration=SensitiveDataScannerConfigurationData(
                data=SensitiveDataScannerConfiguration(
                    type=SensitiveDataScannerConfigurationType.SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
                    id=CONFIGURATION_DATA_ID,
                ),
            ),
            rules=SensitiveDataScannerRuleData(
                data=[],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.create_scanning_group(body=body)

    print(response)
