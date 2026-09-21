"""
Get All Container groups returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.containers_api import ContainersApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ContainersApi(api_client)
    response = api_instance.list_containers(
        group_by="short_image",
    )

    print(response)
