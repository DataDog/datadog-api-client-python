"""
Reorder Groups returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.sensitive_data_scanner_api import SensitiveDataScannerApi
from datadog_api_client.v2.model.sensitive_data_scanner_config_request import SensitiveDataScannerConfigRequest
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_relationships import (
    SensitiveDataScannerConfigurationRelationships,
)
from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import SensitiveDataScannerConfigurationType
from datadog_api_client.v2.model.sensitive_data_scanner_group_item import SensitiveDataScannerGroupItem
from datadog_api_client.v2.model.sensitive_data_scanner_group_list import SensitiveDataScannerGroupList
from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType
from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
from datadog_api_client.v2.model.sensitive_data_scanner_reorder_config import SensitiveDataScannerReorderConfig

# there is a valid "scanning_group" in the system
GROUP_DATA_ID = environ["GROUP_DATA_ID"]

# a valid "configuration" in the system
CONFIGURATION_DATA_ID = environ["CONFIGURATION_DATA_ID"]

body = SensitiveDataScannerConfigRequest(
    data=SensitiveDataScannerReorderConfig(
        relationships=SensitiveDataScannerConfigurationRelationships(
            groups=SensitiveDataScannerGroupList(
                data=[
                    SensitiveDataScannerGroupItem(
                        type=SensitiveDataScannerGroupType.SENSITIVE_DATA_SCANNER_GROUP,
                        id=GROUP_DATA_ID,
                    ),
                ],
            ),
        ),
        type=SensitiveDataScannerConfigurationType.SENSITIVE_DATA_SCANNER_CONFIGURATIONS,
        id=CONFIGURATION_DATA_ID,
    ),
    meta=SensitiveDataScannerMetaVersionOnly(),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SensitiveDataScannerApi(api_client)
    response = api_instance.reorder_scanning_groups(body=body)

    print(response)
