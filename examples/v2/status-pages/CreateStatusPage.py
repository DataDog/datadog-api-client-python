"""
Create status page returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_status_page_request import CreateStatusPageRequest
from datadog_api_client.v2.model.create_status_page_request_data import CreateStatusPageRequestData
from datadog_api_client.v2.model.create_status_page_request_data_attributes import CreateStatusPageRequestDataAttributes
from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
    CreateStatusPageRequestDataAttributesType,
)
from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
    CreateStatusPageRequestDataAttributesVisualizationType,
)
from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

body = CreateStatusPageRequest(
    data=CreateStatusPageRequestData(
        attributes=CreateStatusPageRequestDataAttributes(
            name="[DD Integration Tests] 5e2fd69be33e79aa",
            domain_prefix="dd-integrations-tests-5e2fd69be33e79aa",
            enabled=True,
            type=CreateStatusPageRequestDataAttributesType.INTERNAL,
            visualization_type=CreateStatusPageRequestDataAttributesVisualizationType.BARS_AND_UPTIME_PERCENTAGE,
        ),
        type=StatusPageDataType.STATUS_PAGES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_status_page(body=body)

    print(response)
