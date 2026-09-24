"""
Get all notebooks returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.list_notebooks()

    print(response)
