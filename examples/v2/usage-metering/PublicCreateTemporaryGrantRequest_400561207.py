"""
Create a temporary grant request with a justification
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.temporary_grant_request_create_attributes import TemporaryGrantRequestCreateAttributes
from datadog_api_client.v2.model.temporary_grant_request_create_data import TemporaryGrantRequestCreateData
from datadog_api_client.v2.model.temporary_grant_request_create_request import TemporaryGrantRequestCreateRequest
from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType

body = TemporaryGrantRequestCreateRequest(
    data=TemporaryGrantRequestCreateData(
        type=TemporaryGrantRequestType.TEMPORARY_GRANT_REQUESTS,
        attributes=TemporaryGrantRequestCreateAttributes(
            total=200,
            justification="SDK temporary grant request test",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["public_create_temporary_grant_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.public_create_temporary_grant_request(body=body)

    print(response)
