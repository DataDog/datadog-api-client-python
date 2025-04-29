"""
List pipelines returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi

configuration = Configuration()
configuration.unstable_operations["list_pipelines"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.list_pipelines()

    print(response)
