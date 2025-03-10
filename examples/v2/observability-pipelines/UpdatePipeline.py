"""
Update a specific pipeline returns "Pipeline updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.pipeline import Pipeline
from datadog_api_client.v2.model.pipeline_data import PipelineData
from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes
from datadog_api_client.v2.model.pipeline_data_attributes_config import PipelineDataAttributesConfig

body = Pipeline(
    data=PipelineData(
        attributes=PipelineDataAttributes(
            config=PipelineDataAttributesConfig(
                destinations=[],
                processors=[],
                sources=[],
            ),
            name="",
        ),
        id="e8890e15-053e-4d34-9404-1b41b9e403e2",
        type="pipeline",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.update_pipeline(pipeline_id="pipeline_id", body=body)

    print(response)
