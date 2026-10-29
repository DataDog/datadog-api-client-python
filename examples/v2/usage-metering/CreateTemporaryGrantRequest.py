"""
Create a temporary grant request returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.temporary_grant_request_create_attributes import TemporaryGrantRequestCreateAttributes
from datadog_api_client.v2.model.temporary_grant_request_create_data import TemporaryGrantRequestCreateData
from datadog_api_client.v2.model.temporary_grant_request_create_request import TemporaryGrantRequestCreateRequest
from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType
from datetime import datetime
from dateutil.tz import tzutc

body = TemporaryGrantRequestCreateRequest(
    data=TemporaryGrantRequestCreateData(
        attributes=TemporaryGrantRequestCreateAttributes(
            expires_at=datetime(2028, 2, 16, 0, 0, tzinfo=tzutc()),
            justification="Credits needed to finish the incident investigation.",
            total=200,
        ),
        type=TemporaryGrantRequestType.TEMPORARY_GRANT_REQUESTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_temporary_grant_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.create_temporary_grant_request(body=body)

    print(response)
