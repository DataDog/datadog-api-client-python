"""
Update App Protection Level returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_protection_level import AppProtectionLevel
from datadog_api_client.v2.model.app_protection_level_type import AppProtectionLevelType
from datadog_api_client.v2.model.update_app_protection_level_request import UpdateAppProtectionLevelRequest
from datadog_api_client.v2.model.update_app_protection_level_request_data import UpdateAppProtectionLevelRequestData
from datadog_api_client.v2.model.update_app_protection_level_request_data_attributes import (
    UpdateAppProtectionLevelRequestDataAttributes,
)
from uuid import UUID

body = UpdateAppProtectionLevelRequest(
    data=UpdateAppProtectionLevelRequestData(
        attributes=UpdateAppProtectionLevelRequestDataAttributes(
            protection_level=AppProtectionLevel.APPROVAL_REQUIRED,
        ),
        type=AppProtectionLevelType.PROTECTIONLEVEL,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.update_protection_level(app_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
