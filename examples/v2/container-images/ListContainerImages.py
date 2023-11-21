"""
Get all Container Images returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.container_images_api import ContainerImagesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ContainerImagesApi(api_client)
    response = api_instance.list_container_images()

    print(response)
