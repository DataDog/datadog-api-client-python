"""
Validate an observability pipeline with source secret key returns "OK" response
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
from datadog_api_client.v2.model.observability_pipeline_http_client_source import ObservabilityPipelineHttpClientSource
from datadog_api_client.v2.model.observability_pipeline_http_client_source_auth_strategy import (
    ObservabilityPipelineHttpClientSourceAuthStrategy,
)
from datadog_api_client.v2.model.observability_pipeline_http_client_source_type import (
    ObservabilityPipelineHttpClientSourceType,
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
                            "http-client-source",
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
                    ObservabilityPipelineHttpClientSource(
                        id="http-client-source",
                        type=ObservabilityPipelineHttpClientSourceType.HTTP_CLIENT,
                        decoding=ObservabilityPipelineDecoding.DECODE_BYTES,
                        scrape_interval_secs=15,
                        scrape_timeout_secs=5,
                        auth_strategy=ObservabilityPipelineHttpClientSourceAuthStrategy.BEARER,
                        token_key="HTTP_CLIENT_TOKEN",
                    ),
                ],
            ),
            name="Pipeline with Source Secret",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
