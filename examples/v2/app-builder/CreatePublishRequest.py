"""
Create Publish Request returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.create_publish_request_request import CreatePublishRequestRequest
from datadog_api_client.v2.model.create_publish_request_request_data import CreatePublishRequestRequestData
from datadog_api_client.v2.model.create_publish_request_request_data_attributes import (
    CreatePublishRequestRequestDataAttributes,
)
from datadog_api_client.v2.model.publish_request_type import PublishRequestType
from uuid import UUID

body = CreatePublishRequestRequest(
    data=CreatePublishRequestRequestData(
        attributes=CreatePublishRequestRequestDataAttributes(
            description="Adds new dashboard widgets and a few bug fixes.",
            title="Release v1.2 to production",
        ),
        type=PublishRequestType.PUBLISHREQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.create_publish_request(app_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
