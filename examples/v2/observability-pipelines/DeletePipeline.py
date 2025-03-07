"""
Delete a specific pipeline returns "Pipeline deleted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    api_instance.delete_pipeline(
        pipeline_id="pipeline_id",
    )
