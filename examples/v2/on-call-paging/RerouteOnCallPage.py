"""
Reroute On-Call Page returns "No Content." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from datadog_api_client.v2.model.create_page_request_data_attributes_target import CreatePageRequestDataAttributesTarget
from datadog_api_client.v2.model.on_call_page_target_type import OnCallPageTargetType
from datadog_api_client.v2.model.reroute_on_call_page_request import RerouteOnCallPageRequest
from datadog_api_client.v2.model.reroute_on_call_page_request_data import RerouteOnCallPageRequestData
from datadog_api_client.v2.model.reroute_on_call_page_request_data_attributes import (
    RerouteOnCallPageRequestDataAttributes,
)
from datadog_api_client.v2.model.reroute_on_call_page_request_data_type import RerouteOnCallPageRequestDataType
from uuid import UUID

body = RerouteOnCallPageRequest(
    data=RerouteOnCallPageRequestData(
        attributes=RerouteOnCallPageRequestDataAttributes(
            comment="Rerouting to the database team.",
            target=CreatePageRequestDataAttributesTarget(
                identifier="my-team",
                type=OnCallPageTargetType.TEAM_HANDLE,
            ),
        ),
        type=RerouteOnCallPageRequestDataType.REROUTE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    api_instance.reroute_on_call_page(page_id=UUID("15e74b8b-f865-48d0-bcc5-453323ed2c8f"), body=body)
