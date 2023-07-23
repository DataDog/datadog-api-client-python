"""
Update Confluent account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi
from datadog_api_client.v2.model.confluent_account_update_request import ConfluentAccountUpdateRequestJSON

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY = environ["CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY"]
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

body = ConfluentAccountUpdateRequestJSON(
    api_key=CONFLUENT_ACCOUNT_DATA_ATTRIBUTES_API_KEY,
    api_secret="update-secret",
    tags=[
        "updated_tag:val",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    response = api_instance.update_confluent_account(account_id=CONFLUENT_ACCOUNT_DATA_ID, body=body)

    print(response)
