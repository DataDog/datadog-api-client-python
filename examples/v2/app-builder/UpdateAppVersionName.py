"""
Name App Version returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_version_name_type import AppVersionNameType
from datadog_api_client.v2.model.update_app_version_name_request import UpdateAppVersionNameRequest
from datadog_api_client.v2.model.update_app_version_name_request_data import UpdateAppVersionNameRequestData
from datadog_api_client.v2.model.update_app_version_name_request_data_attributes import (
    UpdateAppVersionNameRequestDataAttributes,
)
from uuid import UUID

body = UpdateAppVersionNameRequest(
    data=UpdateAppVersionNameRequestData(
        attributes=UpdateAppVersionNameRequestDataAttributes(
            name="v1.2.0 - bug fix release",
        ),
        type=AppVersionNameType.VERSIONNAMES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    api_instance.update_app_version_name(
        app_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), version="version", body=body
    )
