"""
Delete resource from Confluent account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

# there is a valid "confluent_account" in the system
CONFLUENT_ACCOUNT_DATA_ID = environ["CONFLUENT_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    api_instance.delete_confluent_account(
        account_id=CONFLUENT_ACCOUNT_DATA_ID,
    )
