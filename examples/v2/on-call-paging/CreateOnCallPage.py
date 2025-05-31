"""
Create On-Call Page returns "OK." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from datadog_api_client.v2.model.create_page_request import CreatePageRequest
from datadog_api_client.v2.model.create_page_request_data import CreatePageRequestData
from datadog_api_client.v2.model.create_page_request_data_attributes import CreatePageRequestDataAttributes
from datadog_api_client.v2.model.create_page_request_data_attributes_target import CreatePageRequestDataAttributesTarget
from datadog_api_client.v2.model.create_page_request_data_type import CreatePageRequestDataType
from datadog_api_client.v2.model.on_call_page_target_type import OnCallPageTargetType
from datadog_api_client.v2.model.page_urgency import PageUrgency

body = CreatePageRequest(
    data=CreatePageRequestData(
        attributes=CreatePageRequestDataAttributes(
            description="Page details.",
            tags=[
                "service:test",
            ],
            target=CreatePageRequestDataAttributesTarget(
                identifier="my-team",
                type=OnCallPageTargetType.TEAM_HANDLE,
            ),
            title="Page title",
            urgency=PageUrgency.LOW,
        ),
        type=CreatePageRequestDataType.PAGES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    response = api_instance.create_on_call_page(body=body)

    print(response)
