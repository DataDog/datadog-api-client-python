"""
Update the tags for an interface returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi
from datadog_api_client.v2.model.list_interface_tags_response import ListInterfaceTagsResponse
from datadog_api_client.v2.model.list_interface_tags_response_data import ListInterfaceTagsResponseData
from datadog_api_client.v2.model.list_tags_response_data_attributes import ListTagsResponseDataAttributes

body = ListInterfaceTagsResponse(
    data=ListInterfaceTagsResponseData(
        attributes=ListTagsResponseDataAttributes(
            tags=[
                "tag:test",
                "tag:testbis",
            ],
        ),
        id="example:1.2.3.4:1",
        type="tags",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.update_interface_user_tags(interface_id="example:1.2.3.4:1", body=body)

    print(response)
