"""
Validate an observability pipeline with enrichment table secret field lookup returns "OK" response
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
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_secret_lookup import (
    ObservabilityPipelineEnrichmentTableFieldSecretLookup,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file import (
    ObservabilityPipelineEnrichmentTableFile,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding import (
    ObservabilityPipelineEnrichmentTableFileEncoding,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding_type import (
    ObservabilityPipelineEnrichmentTableFileEncodingType,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items import (
    ObservabilityPipelineEnrichmentTableFileKeyItems,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items_comparison import (
    ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_schema_items import (
    ObservabilityPipelineEnrichmentTableFileSchemaItems,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_schema_items_type import (
    ObservabilityPipelineEnrichmentTableFileSchemaItemsType,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor import (
    ObservabilityPipelineEnrichmentTableProcessor,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor_type import (
    ObservabilityPipelineEnrichmentTableProcessorType,
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
                            ObservabilityPipelineEnrichmentTableProcessor(
                                enabled=True,
                                id="enrichment-processor",
                                include="*",
                                target="enriched",
                                type=ObservabilityPipelineEnrichmentTableProcessorType.ENRICHMENT_TABLE,
                                file=ObservabilityPipelineEnrichmentTableFile(
                                    encoding=ObservabilityPipelineEnrichmentTableFileEncoding(
                                        delimiter=",",
                                        type=ObservabilityPipelineEnrichmentTableFileEncodingType.CSV,
                                        includes_headers=True,
                                    ),
                                    key=[
                                        ObservabilityPipelineEnrichmentTableFileKeyItems(
                                            column="user_id",
                                            comparison=ObservabilityPipelineEnrichmentTableFileKeyItemsComparison.EQUALS,
                                            field=ObservabilityPipelineEnrichmentTableFieldSecretLookup(
                                                secret="LOOKUP_KEY_SECRET",
                                            ),
                                        ),
                                    ],
                                    path="/etc/enrichment/lookup.csv",
                                    schema=[
                                        ObservabilityPipelineEnrichmentTableFileSchemaItems(
                                            column="user_id",
                                            type=ObservabilityPipelineEnrichmentTableFileSchemaItemsType.STRING,
                                        ),
                                    ],
                                ),
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
            name="Pipeline with Enrichment Table Secret Field Lookup",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
