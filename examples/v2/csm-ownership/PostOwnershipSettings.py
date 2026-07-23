"""
Update ownership settings for the org returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi
from datadog_api_client.v2.model.ownership_confidence_level import OwnershipConfidenceLevel
from datadog_api_client.v2.model.ownership_settings_request import OwnershipSettingsRequest
from datadog_api_client.v2.model.ownership_settings_request_attributes import OwnershipSettingsRequestAttributes
from datadog_api_client.v2.model.ownership_settings_request_data import OwnershipSettingsRequestData
from datadog_api_client.v2.model.ownership_settings_type import OwnershipSettingsType

body = OwnershipSettingsRequest(
    data=OwnershipSettingsRequestData(
        attributes=OwnershipSettingsRequestAttributes(
            auto_tag=True,
            confidence_level=OwnershipConfidenceLevel.HIGH,
        ),
        type=OwnershipSettingsType.OWNERSHIP_SETTINGS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["post_ownership_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.post_ownership_settings(body=body)

    print(response)
