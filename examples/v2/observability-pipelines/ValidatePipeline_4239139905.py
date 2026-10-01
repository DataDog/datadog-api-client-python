"""
Validate a metrics pipeline with enrichment table processor reference table returns "OK" response
"""

from os import environ
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
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
    ObservabilityPipelineDatadogAgentSource,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source_type import (
    ObservabilityPipelineDatadogAgentSourceType,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_metrics_destination import (
    ObservabilityPipelineDatadogMetricsDestination,
)
from datadog_api_client.v2.model.observability_pipeline_datadog_metrics_destination_type import (
    ObservabilityPipelineDatadogMetricsDestinationType,
)
from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor_type import (
    ObservabilityPipelineEnrichmentTableProcessorType,
)
from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_metric_name_lookup import (
    ObservabilityPipelineMetricEnrichmentTableMetricNameLookup,
)
from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_metric_name_lookup_type import (
    ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType,
)
from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_reference_key import (
    ObservabilityPipelineMetricEnrichmentTableReferenceKey,
)
from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_reference_table import (
    ObservabilityPipelineMetricEnrichmentTableReferenceTable,
)
from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_reference_table_processor import (
    ObservabilityPipelineMetricEnrichmentTableReferenceTableProcessor,
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
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineMetricEnrichmentTableReferenceTableProcessor(
                                enabled=True,
                                id="enrichment-table-processor",
                                include="*",
                                type=ObservabilityPipelineEnrichmentTableProcessorType.ENRICHMENT_TABLE,
                                reference_table=ObservabilityPipelineMetricEnrichmentTableReferenceTable(
                                    table_id="metric-enrichment",
                                    key=ObservabilityPipelineMetricEnrichmentTableReferenceKey(
                                        source=ObservabilityPipelineMetricEnrichmentTableMetricNameLookup(
                                            type=ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType.METRIC_NAME,
                                        ),
                                    ),
                                    columns=[
                                        "environment",
                                        "team",
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
            name="Metrics Pipeline with Enrichment Table Reference Table",
        ),
        type="pipelines",
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ObservabilityPipelinesApi(api_client)
    response = api_instance.validate_pipeline(body=body)

    print(response)
