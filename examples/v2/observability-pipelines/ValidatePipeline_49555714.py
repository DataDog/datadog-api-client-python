"""
Validate an observability pipeline with amazon_s3_generic destination SSE-KMS encryption returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_server_side_encryption import (
    ObservabilityPipelineAmazonS3DestinationServerSideEncryption,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_storage_class import (
    ObservabilityPipelineAmazonS3DestinationStorageClass,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_gzip import (
    ObservabilityPipelineAmazonS3GenericCompressionGzip,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_gzip_type import (
    ObservabilityPipelineAmazonS3GenericCompressionGzipType,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_destination import (
    ObservabilityPipelineAmazonS3GenericDestination,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_destination_type import (
    ObservabilityPipelineAmazonS3GenericDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_json import (
    ObservabilityPipelineAmazonS3GenericEncodingJson,
)
from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_json_type import (
    ObservabilityPipelineAmazonS3GenericEncodingJsonType,
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
                    ObservabilityPipelineAmazonS3GenericDestination(
                        id="generic-s3-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineAmazonS3GenericDestinationType.GENERIC_ARCHIVES_S3,
                        bucket="my-bucket",
                        region="us-east-1",
                        storage_class=ObservabilityPipelineAmazonS3DestinationStorageClass.STANDARD,
                        encoding=ObservabilityPipelineAmazonS3GenericEncodingJson(
                            type=ObservabilityPipelineAmazonS3GenericEncodingJsonType.JSON,
                        ),
                        compression=ObservabilityPipelineAmazonS3GenericCompressionGzip(
                            algorithm=ObservabilityPipelineAmazonS3GenericCompressionGzipType.GZIP,
                            level=6,
                        ),
                        server_side_encryption=ObservabilityPipelineAmazonS3DestinationServerSideEncryption.AWS_KMS,
                        ssekms_key_id="arn:aws:kms:us-east-1:123456789012:key/mrk-abc123",
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
            name="Pipeline with S3 Generic SSE-KMS",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
