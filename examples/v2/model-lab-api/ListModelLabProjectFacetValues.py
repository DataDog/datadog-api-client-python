"""
List Model Lab project facet values returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.model_lab_api_api import ModelLabAPIApi
from datadog_api_client.v2.model.model_lab_project_facet_type import ModelLabProjectFacetType

configuration = Configuration()
configuration.unstable_operations["list_model_lab_project_facet_values"] = True
with ApiClient(configuration) as api_client:
    api_instance = ModelLabAPIApi(api_client)
    response = api_instance.list_model_lab_project_facet_values(
        facet_type=ModelLabProjectFacetType.TAG,
        facet_name="model",
    )

    print(response)
