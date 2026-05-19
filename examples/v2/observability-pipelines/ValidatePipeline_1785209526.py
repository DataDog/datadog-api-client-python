"""
Validate an observability pipeline with HTTP server source valid_tokens returns "OK" response
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
from datadog_api_client.v2.model.observability_pipeline_http_server_source import ObservabilityPipelineHttpServerSource
from datadog_api_client.v2.model.observability_pipeline_http_server_source_auth_strategy import (
    ObservabilityPipelineHttpServerSourceAuthStrategy,
)
from datadog_api_client.v2.model.observability_pipeline_http_server_source_type import (
    ObservabilityPipelineHttpServerSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token import (
    ObservabilityPipelineHttpServerSourceValidToken,
)
from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token_path_to_token_header import (
    ObservabilityPipelineHttpServerSourceValidTokenPathToTokenHeader,
)
from datadog_api_client.v2.model.observability_pipeline_source_valid_token_field_to_add import (
    ObservabilityPipelineSourceValidTokenFieldToAdd,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData

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
                            "http-server-source",
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
                    ObservabilityPipelineHttpServerSource(
                        id="http-server-source",
                        type=ObservabilityPipelineHttpServerSourceType.HTTP_SERVER,
                        auth_strategy=ObservabilityPipelineHttpServerSourceAuthStrategy.NONE,
                        decoding=ObservabilityPipelineDecoding.DECODE_JSON,
                        valid_tokens=[
                            ObservabilityPipelineHttpServerSourceValidToken(
                                token_key="HTTP_SERVER_TOKEN",
                                enabled=True,
                                path_to_token=ObservabilityPipelineHttpServerSourceValidTokenPathToTokenHeader(
                                    header="X-Token",
                                ),
                                field_to_add=ObservabilityPipelineSourceValidTokenFieldToAdd(
                                    key="token_name",
                                    value="primary_token",
                                ),
                            ),
                            ObservabilityPipelineHttpServerSourceValidToken(
                                token_key="HTTP_SERVER_TOKEN_BACKUP",
                                enabled=True,
                                path_to_token="path",
                            ),
                        ],
                    ),
                ],
            ),
            name="Pipeline with HTTP server valid_tokens",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
