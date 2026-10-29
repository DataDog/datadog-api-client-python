"""
Get service repository information returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.service_repository_info_data_type import ServiceRepositoryInfoDataType
from datadog_api_client.v2.model.service_repository_info_request import ServiceRepositoryInfoRequest
from datadog_api_client.v2.model.service_repository_info_request_attributes import (
    ServiceRepositoryInfoRequestAttributes,
)
from datadog_api_client.v2.model.service_repository_info_request_data import ServiceRepositoryInfoRequestData
from uuid import UUID

body = ServiceRepositoryInfoRequest(
    data=ServiceRepositoryInfoRequestData(
        attributes=ServiceRepositoryInfoRequestAttributes(
            debug_id=UUID("00000000-0000-4000-8000-000000000001"),
        ),
        type=ServiceRepositoryInfoDataType.SERVICE_REPOSITORY_INFO,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_service_repository_info"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.get_service_repository_info(body=body)

    print(response)
