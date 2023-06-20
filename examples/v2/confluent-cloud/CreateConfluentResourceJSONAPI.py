"""
Add resource to Confluent account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_resource_request import ConfluentResourceRequestJSON

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

body = ConfluentResourceRequestJSON(
    resource_type="kafka",
    tags=[
        "myTag",
        "myTag2:myValue",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.create_confluent_resource(account_id=CONFLUENT_ACCOUNT_DATA_ID, body=body)

    print(response)
