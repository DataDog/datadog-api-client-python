"""
Add Confluent account returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_account_create_request import ConfluentAccountCreateRequestJSON
from datadog_api_client.v2.model.confluent_account_resource_attributes import ConfluentAccountResourceAttributes

body = ConfluentAccountCreateRequestJSON(
    api_key="TESTAPIKEY123",
    api_secret="test-api-secret-123",
    resources=[
        ConfluentAccountResourceAttributes(
            id="resource-id-123",
            resource_type="kafka",
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
    ],
    tags=[
        "myTag",
        "myTag2:myValue",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.create_confluent_account(body=body)

    print(response)
