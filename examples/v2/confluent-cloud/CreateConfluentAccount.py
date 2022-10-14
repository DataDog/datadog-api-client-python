"""
Add Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_account_create_request import ConfluentAccountCreateRequest
from datadog_api_client.v2.model.confluent_account_create_request_attributes import (
    ConfluentAccountCreateRequestAttributes,
)
from datadog_api_client.v2.model.confluent_account_create_request_data import ConfluentAccountCreateRequestData
from datadog_api_client.v2.model.confluent_account_resource_attributes import ConfluentAccountResourceAttributes
from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType

body = ConfluentAccountCreateRequest(
    data=ConfluentAccountCreateRequestData(
        attributes=ConfluentAccountCreateRequestAttributes(
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
        ),
        type=ConfluentAccountType.CONFLUENT_CLOUD_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.create_confluent_account(body=body)

    print(response)
