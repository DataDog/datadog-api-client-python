"""
Validate an observability pipeline with ClickHouse destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination import (
    ObservabilityPipelineClickhouseDestination,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_auth import (
    ObservabilityPipelineClickhouseDestinationAuth,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_auth_strategy import (
    ObservabilityPipelineClickhouseDestinationAuthStrategy,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch import (
    ObservabilityPipelineClickhouseDestinationBatch,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_type import (
    ObservabilityPipelineClickhouseDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
    ObservabilityPipelineConfigProcessorGroup,
)
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
    ObservabilityPipelineDatadogAgentSource,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source_type import (
    ObservabilityPipelineDatadogAgentSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData

body = ObservabilityPipelineSpec(
    data=ObservabilityPipelineSpecData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                destinations=[
                    ObservabilityPipelineClickhouseDestination(
                        id="clickhouse-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineClickhouseDestinationType.CLICKHOUSE,
                        table="application_logs",
                        database="my_database",
                        compression="gzip",
                        auth=ObservabilityPipelineClickhouseDestinationAuth(
                            strategy=ObservabilityPipelineClickhouseDestinationAuthStrategy.BASIC,
                            username_key="CLICKHOUSE_USERNAME",
                            password_key="CLICKHOUSE_PASSWORD",
                        ),
                        batch=ObservabilityPipelineClickhouseDestinationBatch(
                            max_events=1000,
                            timeout_secs=1,
                        ),
                    ),
                ],
                processor_groups=[
                    ObservabilityPipelineConfigProcessorGroup(
                        enabled=True,
                        id="my-processor-group",
                        include="service:my-service",
                        inputs=[
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineFilterProcessor(
                                enabled=True,
                                id="filter-processor",
                                include="status:error",
                                type=ObservabilityPipelineFilterProcessorType.FILTER,
                            ),
                        ],
                    ),
                ],
                sources=[
                    ObservabilityPipelineDatadogAgentSource(
                        id="datadog-agent-source",
                        type=ObservabilityPipelineDatadogAgentSourceType.DATADOG_AGENT,
                    ),
                ],
            ),
            name="Pipeline with ClickHouse Destination",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
