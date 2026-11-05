"""
Delete an email access policy returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.delete_email_access_policy(
        page_id=UUID("1234abcd-12ab-34cd-56ef-123456abcdef"),
        policy_id=UUID("1234abcd-12ab-34cd-56ef-123456abcdef"),
    )
