"""
Validate an observability pipeline with cloud_prem destination buffer returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
from datadog_api_client.v2.model.observability_pipeline_buffer_options_disk_type import (
    ObservabilityPipelineBufferOptionsDiskType,
)
from datadog_api_client.v2.model.observability_pipeline_buffer_options_when_full import (
    ObservabilityPipelineBufferOptionsWhenFull,
)
from datadog_api_client.v2.model.observability_pipeline_cloud_prem_destination import (
    ObservabilityPipelineCloudPremDestination,
)
from datadog_api_client.v2.model.observability_pipeline_cloud_prem_destination_type import (
    ObservabilityPipelineCloudPremDestinationType,
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
from datadog_api_client.v2.model.observability_pipeline_disk_buffer_options import (
    ObservabilityPipelineDiskBufferOptions,
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
                    ObservabilityPipelineCloudPremDestination(
                        id="cloud-prem-destination",
                        inputs=[
                            "my-processor-group",
                        ],
                        type=ObservabilityPipelineCloudPremDestinationType.CLOUD_PREM,
                        endpoint_url_key="CLOUDPREM_ENDPOINT_URL",
                        buffer=ObservabilityPipelineDiskBufferOptions(
                            type=ObservabilityPipelineBufferOptionsDiskType.DISK,
                            max_size=1073741824,
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
            name="Pipeline with CloudPrem Buffer",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
