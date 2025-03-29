"""
Create a new pipeline returns "Pipeline created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.datadog_agent_source import DatadogAgentSource
from datadog_api_client.v2.model.datadog_agent_source_type import DatadogAgentSourceType
from datadog_api_client.v2.model.datadog_logs_destination import DatadogLogsDestination
from datadog_api_client.v2.model.datadog_logs_destination_type import DatadogLogsDestinationType
from datadog_api_client.v2.model.filter_processor import FilterProcessor
from datadog_api_client.v2.model.filter_processor_type import FilterProcessorType
from datadog_api_client.v2.model.pipeline import Pipeline
from datadog_api_client.v2.model.pipeline_data import PipelineData
from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes
from datadog_api_client.v2.model.pipeline_data_attributes_config import PipelineDataAttributesConfig
from datadog_api_client.v2.model.tls import Tls

body = Pipeline(
    data=PipelineData(
        attributes=PipelineDataAttributes(
            config=PipelineDataAttributesConfig(
                destinations=[
                    DatadogLogsDestination(
                        id="",
                        inputs=[
                            "",
                        ],
                        type=DatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processors=[
                    FilterProcessor(
                        id="",
                        include="",
                        inputs=[
                            "",
                        ],
                        type=FilterProcessorType.FILTER,
                    ),
                ],
                sources=[
                    DatadogAgentSource(
                        id="",
                        tls=Tls(
                            crt_file="",
                        ),
                        type=DatadogAgentSourceType.DATADOG_AGENT,
                    ),
                ],
            ),
            name="Main Observability Pipeline",
        ),
        id="pipeline-1",
        type="pipeline",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.create_pipeline(body=body)

    print(response)
