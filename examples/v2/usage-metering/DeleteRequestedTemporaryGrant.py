"""
Revoke a requested temporary grant returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_requested_temporary_grant"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    api_instance.delete_requested_temporary_grant(
        request_id=UUID("12345678-1234-1234-1234-123456789012"),
    )
