"""
Create component returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_component_request import CreateComponentRequest
from datadog_api_client.v2.model.create_component_request_data import CreateComponentRequestData
from datadog_api_client.v2.model.create_component_request_data_attributes import CreateComponentRequestDataAttributes
from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
    CreateComponentRequestDataAttributesType,
)
from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateComponentRequest(
    data=CreateComponentRequestData(
        attributes=CreateComponentRequestDataAttributes(
            name="Logs",
            position=0,
            type=CreateComponentRequestDataAttributesType.COMPONENT,
        ),
        type=StatusPagesComponentGroupType.COMPONENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_component(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
