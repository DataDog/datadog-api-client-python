"""
Delete a notebook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = environ["NOTEBOOK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    api_instance.delete_notebook(
        notebook_id=int(NOTEBOOK_DATA_ID),
    )
