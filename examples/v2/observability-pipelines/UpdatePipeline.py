"""
Update a pipeline returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline import ObservabilityPipeline
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_data import ObservabilityPipelineData
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
    ObservabilityPipelineDatadogAgentSource,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source_type import (
    ObservabilityPipelineDatadogAgentSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
    ObservabilityPipelineDatadogLogsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
    ObservabilityPipelineDatadogLogsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = environ["PIPELINE_DATA_ID"]

body = ObservabilityPipeline(
    data=ObservabilityPipelineData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                destinations=[
                    ObservabilityPipelineDatadogLogsDestination(
                        id="updated-datadog-logs-destination-id",
                        inputs=[
                            "filter-processor",
                        ],
                        type=ObservabilityPipelineDatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processors=[
                    ObservabilityPipelineFilterProcessor(
                        id="filter-processor",
                        include="service:my-service",
                        inputs=[
                            "datadog-agent-source",
                        ],
                        type=ObservabilityPipelineFilterProcessorType.FILTER,
                    ),
                ],
                sources=[
                    ObservabilityPipelineDatadogAgentSource(
                        id="datadog-agent-source",
                        type=ObservabilityPipelineDatadogAgentSourceType.DATADOG_AGENT,
                    ),
                ],
            ),
            name="Updated Pipeline Name",
        ),
        id=PIPELINE_DATA_ID,
        type="pipelines",
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_pipeline"] = True
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.update_pipeline(pipeline_id=PIPELINE_DATA_ID, body=body)

    print(response)
