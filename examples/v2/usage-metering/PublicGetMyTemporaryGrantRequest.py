"""
Get your temporary grant request returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["public_get_my_temporary_grant_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.public_get_my_temporary_grant_request(
        request_id=UUID("12345678-1234-1234-1234-123456789012"),
    )

    print(response)
