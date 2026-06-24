"""
Validate an observability pipeline with websocket source bearer auth returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
    ObservabilityPipelineConfigProcessorGroup,
)
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
    ObservabilityPipelineDatadogLogsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
    ObservabilityPipelineDatadogLogsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData
from datadog_api_client.v2.model.observability_pipeline_websocket_source import ObservabilityPipelineWebsocketSource
from datadog_api_client.v2.model.observability_pipeline_websocket_source_auth_strategy import (
    ObservabilityPipelineWebsocketSourceAuthStrategy,
)
from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_enabled import (
    ObservabilityPipelineWebsocketSourceTlsEnabled,
)
from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_enabled_mode import (
    ObservabilityPipelineWebsocketSourceTlsEnabledMode,
)
from datadog_api_client.v2.model.observability_pipeline_websocket_source_type import (
    ObservabilityPipelineWebsocketSourceType,
)

body = ObservabilityPipelineSpec(
    data=ObservabilityPipelineSpecData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                destinations=[
                    ObservabilityPipelineDatadogLogsDestination(
                        id="datadog-logs-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineDatadogLogsDestinationType.DATADOG_LOGS,
                    ),
                ],
                processor_groups=[
                    ObservabilityPipelineConfigProcessorGroup(
                        enabled=True,
                        id="my-processor-group",
                        include="service:my-service",
                        inputs=[
                            "websocket-source",
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
                    ObservabilityPipelineWebsocketSource(
                        id="websocket-source",
                        type=ObservabilityPipelineWebsocketSourceType.WEBSOCKET,
                        decoding=ObservabilityPipelineDecoding.DECODE_JSON,
                        auth_strategy=ObservabilityPipelineWebsocketSourceAuthStrategy.BEARER,
                        token_key="WS_BEARER_TOKEN",
                        uri_key="WS_URI",
                        tls=ObservabilityPipelineWebsocketSourceTlsEnabled(
                            mode=ObservabilityPipelineWebsocketSourceTlsEnabledMode.ENABLED,
                        ),
                    ),
                ],
            ),
            name="Pipeline with WebSocket Source",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
