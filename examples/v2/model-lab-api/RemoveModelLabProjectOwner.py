"""
Remove an owner from a Model Lab project returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["remove_model_lab_project_owner"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    api_instance.remove_model_lab_project_owner(
        project_id=1,
        user_id=UUID("00000000-0000-0000-0000-000000000001"),
    )
