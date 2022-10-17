"""
Update resource in Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_resource_request import ConfluentResourceRequest
from datadog_api_client.v2.model.confluent_resource_request_attributes import ConfluentResourceRequestAttributes
from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData
from datadog_api_client.v2.model.confluent_resource_type import ConfluentResourceType

body = ConfluentResourceRequest(
    data=ConfluentResourceRequestData(
        attributes=ConfluentResourceRequestAttributes(
            resource_type="kafka",
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        id="resource-id-123",
        type=ConfluentResourceType.CONFLUENT_CLOUD_RESOURCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.update_confluent_resource(account_id="account_id", resource_id="resource_id", body=body)

    print(response)
