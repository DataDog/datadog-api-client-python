"""
Get a Model Lab run returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi

configuration = Configuration()
configuration.unstable_operations["get_model_lab_run"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    response = api_instance.get_model_lab_run(
        run_id=70158,
    )

    print(response)
