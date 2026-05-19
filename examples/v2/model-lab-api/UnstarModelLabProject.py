"""
Remove star from a Model Lab project returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi

configuration = Configuration()
configuration.unstable_operations["unstar_model_lab_project"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    api_instance.unstar_model_lab_project(
        project_id=1,
    )
