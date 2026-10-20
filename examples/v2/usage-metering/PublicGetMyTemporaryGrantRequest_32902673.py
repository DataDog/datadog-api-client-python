"""
Read an owned temporary grant request
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

# there is a valid "temporary_grant_request" in the system
TEMPORARY_GRANT_REQUEST_DATA_ID = environ["TEMPORARY_GRANT_REQUEST_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["public_create_temporary_grant_request"] = True
configuration.unstable_operations["public_get_my_temporary_grant_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.public_get_my_temporary_grant_request(
        request_id=TEMPORARY_GRANT_REQUEST_DATA_ID,
    )

    print(response)
