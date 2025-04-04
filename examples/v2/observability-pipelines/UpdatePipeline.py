"""
Update a pipeline returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.pipeline import Pipeline
from datadog_api_client.v2.model.pipeline_config import PipelineConfig
from datadog_api_client.v2.model.pipeline_data import PipelineData
from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes
from datadog_api_client.v2.model.pipeline_datadog_agent_source import PipelineDatadogAgentSource
from datadog_api_client.v2.model.pipeline_datadog_agent_source_type import PipelineDatadogAgentSourceType
from datadog_api_client.v2.model.pipeline_datadog_logs_destination import PipelineDatadogLogsDestination
from datadog_api_client.v2.model.pipeline_datadog_logs_destination_type import PipelineDatadogLogsDestinationType
from datadog_api_client.v2.model.pipeline_filter_processor import PipelineFilterProcessor
from datadog_api_client.v2.model.pipeline_filter_processor_type import PipelineFilterProcessorType

# there is a valid "pipeline" in the system
PIPELINE_DATA_ID = environ["PIPELINE_DATA_ID"]

body = Pipeline(
    data=PipelineData(
        attributes=PipelineDataAttributes(
            config=PipelineConfig(
                destinations=[
                    PipelineDatadogLogsDestination(
                        id="updated-datadog-logs-destination-id",
                        inputs=[
                            "filter-processor",
                        ],
                        type=PipelineDatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processors=[
                    PipelineFilterProcessor(
                        id="filter-processor",
                        include="service:my-service",
                        inputs=[
                            "datadog-agent-source",
                        ],
                        type=PipelineFilterProcessorType.FILTER,
                    ),
                ],
                sources=[
                    PipelineDatadogAgentSource(
                        id="datadog-agent-source",
                        type=PipelineDatadogAgentSourceType.DATADOG_AGENT,
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
