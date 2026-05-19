"""
List Model Lab project artifacts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi

configuration = Configuration()
configuration.unstable_operations["list_model_lab_project_artifacts"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    response = api_instance.list_model_lab_project_artifacts(
        project_id=2387,
    )

    print(response)
