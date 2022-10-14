"""
Add resource to Confluent account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_resource_request import ConfluentResourceRequest
from datadog_api_client.v2.model.confluent_resource_request_attributes import ConfluentResourceRequestAttributes
from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData
from datadog_api_client.v2.model.confluent_resource_type import ConfluentResourceType

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

body = ConfluentResourceRequest(
    data=ConfluentResourceRequestData(
        attributes=ConfluentResourceRequestAttributes(
            resource_type="kafka",
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        id="exampleaddresourcetoconfluentaccountreturnsokresponse",
        type=ConfluentResourceType.CONFLUENT_CLOUD_RESOURCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.create_confluent_resource(account_id=CONFLUENT_ACCOUNT_DATA_ID, body=body)

    print(response)
