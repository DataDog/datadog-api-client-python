"""
Update resource in Confluent account returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_resource_request import ConfluentResourceRequestJSON

body = ConfluentResourceRequestJSON(
    id="resource-id-123",
    resource_type="kafka",
    tags=[
        "myTag",
        "myTag2:myValue",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.update_confluent_resource(account_id="account_id", resource_id="resource_id", body=body)

    print(response)
