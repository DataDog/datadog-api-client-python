"""
Get Model Lab artifact content returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi

configuration = Configuration()
configuration.unstable_operations["get_model_lab_artifact_content"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    response = api_instance.get_model_lab_artifact_content(
        project_id="1",
        artifact_path="runs/42/model/weights.pt",
    )

    print(response.read())
