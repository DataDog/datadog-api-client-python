"""
Get All Containers returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.containers_api import ContainersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ContainersApi(api_client)
    response = api_instance.list_containers()

    print(response)
