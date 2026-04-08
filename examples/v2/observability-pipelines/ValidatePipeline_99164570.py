"""
Validate an observability pipeline with amazon S3 source compression returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_source import ObservabilityPipelineAmazonS3Source
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_source_compression import (
    ObservabilityPipelineAmazonS3SourceCompression,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_source_type import (
    ObservabilityPipelineAmazonS3SourceType,
)
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
                            "amazon-s3-source",
                        ],
                        processors=[
                            ObservabilityPipelineFilterProcessor(
                                enabled=True,
                                id="filter-processor",
                                include="service:my-service",
                                type=ObservabilityPipelineFilterProcessorType.FILTER,
                            ),
                        ],
                    ),
                ],
                sources=[
                    ObservabilityPipelineAmazonS3Source(
                        id="amazon-s3-source",
                        type=ObservabilityPipelineAmazonS3SourceType.AMAZON_S3,
                        region="us-east-1",
                        compression=ObservabilityPipelineAmazonS3SourceCompression.GZIP,
                    ),
                ],
            ),
            name="Pipeline with S3 Source Compression",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
