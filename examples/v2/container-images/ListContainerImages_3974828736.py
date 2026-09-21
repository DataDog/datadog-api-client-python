"""
Get all Container Image groups returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.container_images_api import ContainerImagesApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ContainerImagesApi(api_client)
    response = api_instance.list_container_images(
        group_by="short_image",
    )

    print(response)
