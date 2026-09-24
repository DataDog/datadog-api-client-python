"""
Get all notebooks returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    items = api_instance.list_notebooks_with_pagination(
        count=2,
    )
    for item in items:
        print(item)
