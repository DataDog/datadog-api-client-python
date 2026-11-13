"""
Create On-Call Page Comment returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.create_on_call_page_comment_request import CreateOnCallPageCommentRequest
from datadog_api_client.v2.model.create_on_call_page_comment_request_attributes import (
    CreateOnCallPageCommentRequestAttributes,
)
from datadog_api_client.v2.model.create_on_call_page_comment_request_data import CreateOnCallPageCommentRequestData
from datadog_api_client.v2.model.on_call_page_comment_type import OnCallPageCommentType
from uuid import UUID

body = CreateOnCallPageCommentRequest(
    data=CreateOnCallPageCommentRequestData(
        attributes=CreateOnCallPageCommentRequestAttributes(
            body="Comment from the API client integration tests.",
        ),
        id=UUID("3c5f5b5e-3a3e-4f8c-9b1d-2f6a7e8d9c0b"),
        type=OnCallPageCommentType.COMMENTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.create_on_call_page_comment(page_id="f63eb677-07ce-46ab-b2e0-80ca1ffe91bf", body=body)
