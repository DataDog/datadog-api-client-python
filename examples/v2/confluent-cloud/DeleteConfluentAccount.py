"""
Delete Confluent account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.confluent_cloud_api import ConfluentCloudApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ConfluentCloudApi(api_client)
    api_instance.delete_confluent_account(
        account_id="account_id",
    )
