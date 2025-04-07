"""
Get a specific pipeline returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = environ["PIPELINE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.get_pipeline(
        pipeline_id=PIPELINE_DATA_ID,
    )

    print(response)
