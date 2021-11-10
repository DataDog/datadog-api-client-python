"""
Get all notebooks returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

with ApiClient(Configuration()) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.list_notebooks()

    print(response)
