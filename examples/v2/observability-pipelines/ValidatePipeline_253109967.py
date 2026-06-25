"""
Validate an observability pipeline with ClickHouse destination with all fields set returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_buffer_options_memory_type import (
    ObservabilityPipelineBufferOptionsMemoryType,
)
from datadog_api_client.v2.model.observability_pipeline_buffer_options_when_full import (
    ObservabilityPipelineBufferOptionsWhenFull,
)
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
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch_encoding import (
    ObservabilityPipelineClickhouseDestinationBatchEncoding,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch_encoding_codec import (
    ObservabilityPipelineClickhouseDestinationBatchEncodingCodec,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression_algorithm import (
    ObservabilityPipelineClickhouseDestinationCompressionAlgorithm,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression_object import (
    ObservabilityPipelineClickhouseDestinationCompressionObject,
)
from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_format import (
    ObservabilityPipelineClickhouseDestinationFormat,
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
from datadog_api_client.v2.model.observability_pipeline_memory_buffer_size_options import (
    ObservabilityPipelineMemoryBufferSizeOptions,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData
from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls

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
                        endpoint_url_key="CLICKHOUSE_ENDPOINT_URL",
                        database="my_database",
                        table="application_logs",
                        format=ObservabilityPipelineClickhouseDestinationFormat.ARROW_STREAM,
                        skip_unknown_fields=True,
                        date_time_best_effort=True,
                        compression=ObservabilityPipelineClickhouseDestinationCompressionObject(
                            algorithm=ObservabilityPipelineClickhouseDestinationCompressionAlgorithm.GZIP,
                            level=6,
                        ),
                        auth=ObservabilityPipelineClickhouseDestinationAuth(
                            strategy=ObservabilityPipelineClickhouseDestinationAuthStrategy.BASIC,
                            username_key="CLICKHOUSE_USERNAME",
                            password_key="CLICKHOUSE_PASSWORD",
                        ),
                        batch=ObservabilityPipelineClickhouseDestinationBatch(
                            max_events=1000,
                            timeout_secs=1,
                        ),
                        batch_encoding=ObservabilityPipelineClickhouseDestinationBatchEncoding(
                            codec=ObservabilityPipelineClickhouseDestinationBatchEncodingCodec.ARROW_STREAM,
                            allow_nullable_fields=True,
                        ),
                        tls=ObservabilityPipelineTls(
                            crt_file="/path/to/cert.crt",
                            ca_file="/path/to/ca.crt",
                            key_file="/path/to/key.key",
                            key_pass_key="TLS_KEY_PASSPHRASE",
                        ),
                        buffer=ObservabilityPipelineMemoryBufferSizeOptions(
                            type=ObservabilityPipelineBufferOptionsMemoryType.MEMORY,
                            max_events=500,
                            when_full=ObservabilityPipelineBufferOptionsWhenFull.BLOCK,
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
            name="Pipeline with ClickHouse Destination All Fields",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
