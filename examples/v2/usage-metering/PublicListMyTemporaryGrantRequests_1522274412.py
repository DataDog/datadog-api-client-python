"""
List your pending temporary grant requests
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.temporary_grant_request_status import TemporaryGrantRequestStatus

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["public_list_my_temporary_grant_requests"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.public_list_my_temporary_grant_requests(
        filter_status=TemporaryGrantRequestStatus.PENDING,
        page_limit=1,
    )

    print(response)
