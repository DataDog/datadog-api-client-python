"""
Get All Containers returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.containers_api import ContainersApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ContainersApi(api_client)
    items = api_instance.list_containers_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
