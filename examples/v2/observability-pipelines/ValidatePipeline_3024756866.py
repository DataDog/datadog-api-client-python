"""
Validate an observability pipeline with OCSF mapper custom mapping returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.observability_pipelines_api import ObservabilityPipelinesApi
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
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
    ObservabilityPipelineDatadogLogsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
    ObservabilityPipelineDatadogLogsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor import (
    ObservabilityPipelineOcsfMapperProcessor,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_mapping import (
    ObservabilityPipelineOcsfMapperProcessorMapping,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_type import (
    ObservabilityPipelineOcsfMapperProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom import (
    ObservabilityPipelineOcsfMappingCustom,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_field_mapping import (
    ObservabilityPipelineOcsfMappingCustomFieldMapping,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_lookup import (
    ObservabilityPipelineOcsfMappingCustomLookup,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_lookup_table_entry import (
    ObservabilityPipelineOcsfMappingCustomLookupTableEntry,
)
from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_metadata import (
    ObservabilityPipelineOcsfMappingCustomMetadata,
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
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineOcsfMapperProcessor(
                                enabled=True,
                                id="ocsf-mapper-processor",
                                include="service:my-service",
                                mappings=[
                                    ObservabilityPipelineOcsfMapperProcessorMapping(
                                        include="source:custom",
                                        mapping=ObservabilityPipelineOcsfMappingCustom(
                                            mapping=[
                                                ObservabilityPipelineOcsfMappingCustomFieldMapping(
                                                    default="",
                                                    dest="time",
                                                    source="timestamp",
                                                ),
                                                ObservabilityPipelineOcsfMappingCustomFieldMapping(
                                                    default="",
                                                    dest="severity",
                                                    source="level",
                                                ),
                                                ObservabilityPipelineOcsfMappingCustomFieldMapping(
                                                    default="",
                                                    dest="device.type",
                                                    lookup=ObservabilityPipelineOcsfMappingCustomLookup(
                                                        table=[
                                                            ObservabilityPipelineOcsfMappingCustomLookupTableEntry(
                                                                contains="Desktop",
                                                                value="desktop",
                                                            ),
                                                        ],
                                                    ),
                                                    source="host.type",
                                                ),
                                            ],
                                            metadata=ObservabilityPipelineOcsfMappingCustomMetadata(
                                                _class="Device Inventory Info",
                                                profiles=[
                                                    "container",
                                                ],
                                                version="1.3.0",
                                            ),
                                            version=1,
                                        ),
                                    ),
                                ],
                                type=ObservabilityPipelineOcsfMapperProcessorType.OCSF_MAPPER,
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
            name="OCSF Custom Mapper Pipeline",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
