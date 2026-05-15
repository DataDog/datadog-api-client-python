"""
Update App Tags returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_tags_type import AppTagsType
from datadog_api_client.v2.model.update_app_tags_request import UpdateAppTagsRequest
from datadog_api_client.v2.model.update_app_tags_request_data import UpdateAppTagsRequestData
from datadog_api_client.v2.model.update_app_tags_request_data_attributes import UpdateAppTagsRequestDataAttributes
from uuid import UUID

body = UpdateAppTagsRequest(
    data=UpdateAppTagsRequestData(
        attributes=UpdateAppTagsRequestDataAttributes(
            tags=[
                "team:platform",
                "service:ops",
            ],
        ),
        type=AppTagsType.TAGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    api_instance.update_app_tags(app_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)
