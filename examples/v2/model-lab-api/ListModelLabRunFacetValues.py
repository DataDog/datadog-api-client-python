"""
List Model Lab run facet values returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi
from datadog_api_client.v2.model.model_lab_facet_type import ModelLabFacetType

configuration = Configuration()
configuration.unstable_operations["list_model_lab_run_facet_values"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    response = api_instance.list_model_lab_run_facet_values(
        filter_project_id=2387,
        facet_type=ModelLabFacetType.TAG,
        facet_name="model",
    )

    print(response)
