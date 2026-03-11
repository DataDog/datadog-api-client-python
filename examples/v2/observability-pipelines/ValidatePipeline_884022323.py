"""
Validate a metrics pipeline with opentelemetry source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig
from datadog_api_client.v2.model.observability_pipeline_config_pipeline_type import (
    ObservabilityPipelineConfigPipelineType,
)
from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
    ObservabilityPipelineConfigProcessorGroup,
)
from datadog_api_client.v2.model.observability_pipeline_data_attributes import ObservabilityPipelineDataAttributes
from datadog_api_client.v2.model.observability_pipeline_datadog_metrics_destination import (
    ObservabilityPipelineDatadogMetricsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_metrics_destination_type import (
    ObservabilityPipelineDatadogMetricsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
    ObservabilityPipelineFilterProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_opentelemetry_source import (
    ObservabilityPipelineOpentelemetrySource,
)
from datadog_api_client.v2.model.observability_pipeline_opentelemetry_source_type import (
    ObservabilityPipelineOpentelemetrySourceType,
)
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData

body = ObservabilityPipelineSpec(
    data=ObservabilityPipelineSpecData(
        attributes=ObservabilityPipelineDataAttributes(
            config=ObservabilityPipelineConfig(
                pipeline_type=ObservabilityPipelineConfigPipelineType.METRICS,
                destinations=[
                    ObservabilityPipelineDatadogMetricsDestination(
                        id="datadog-metrics-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineDatadogMetricsDestinationType.DATADOG_METRICS,
                    ),
                ],
                processor_groups=[
                    ObservabilityPipelineConfigProcessorGroup(
                        enabled=True,
                        id="my-processor-group",
                        include="*",
                        inputs=[
                            "opentelemetry-source",
                        ],
                        processors=[
                            ObservabilityPipelineFilterProcessor(
                                enabled=True,
                                id="filter-processor",
                                include="env:production",
                                type=ObservabilityPipelineFilterProcessorType.FILTER,
                            ),
                        ],
                    ),
                ],
                sources=[
                    ObservabilityPipelineOpentelemetrySource(
                        id="opentelemetry-source",
                        type=ObservabilityPipelineOpentelemetrySourceType.OPENTELEMETRY,
                    ),
                ],
            ),
            name="Metrics OTel Pipeline",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
