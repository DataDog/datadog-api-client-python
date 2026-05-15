"""
Update App Self-Service Status returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_self_service_type import AppSelfServiceType
from datadog_api_client.v2.model.update_app_self_service_request import UpdateAppSelfServiceRequest
from datadog_api_client.v2.model.update_app_self_service_request_data import UpdateAppSelfServiceRequestData
from datadog_api_client.v2.model.update_app_self_service_request_data_attributes import (
    UpdateAppSelfServiceRequestDataAttributes,
)
from uuid import UUID

body = UpdateAppSelfServiceRequest(
    data=UpdateAppSelfServiceRequestData(
        attributes=UpdateAppSelfServiceRequestDataAttributes(
            self_service=True,
        ),
        type=AppSelfServiceType.SELFSERVICE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    api_instance.update_app_self_service(app_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)
