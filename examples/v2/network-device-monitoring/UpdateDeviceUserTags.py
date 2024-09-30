"""
Update the tags for a device returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.network_device_monitoring_api import NetworkDeviceMonitoringApi
from datadog_api_client.v2.model.list_tags_response import ListTagsResponse
from datadog_api_client.v2.model.list_tags_response_data import ListTagsResponseData
from datadog_api_client.v2.model.list_tags_response_data_attributes import ListTagsResponseDataAttributes

body = ListTagsResponse(
    data=ListTagsResponseData(
        attributes=ListTagsResponseDataAttributes(
            tags=[
                "tag:test",
                "tag:testbis",
            ],
        ),
        id="default_device",
        type="tags",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NetworkDeviceMonitoringApi(api_client)
    response = api_instance.update_device_user_tags(device_id="default_device", body=body)

    print(response)
