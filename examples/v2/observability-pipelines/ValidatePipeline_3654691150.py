"""
Validate an observability pipeline with spike protection processor threshold overrides returns "OK" response
"""

from os import environ
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
from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor import (
    ObservabilityPipelineSpikeProtectionProcessor,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_action_when_missing_partitions import (
    ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_always_keep import (
    ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeep,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_always_keep_type import (
    ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_bytes import (
    ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytes,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_bytes_type import (
    ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_spike_action import (
    ObservabilityPipelineSpikeProtectionProcessorSpikeAction,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_threshold_override import (
    ObservabilityPipelineSpikeProtectionProcessorThresholdOverride,
)
from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_type import (
    ObservabilityPipelineSpikeProtectionProcessorType,
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
                            "datadog-agent-source",
                        ],
                        processors=[
                            ObservabilityPipelineSpikeProtectionProcessor(
                                enabled=True,
                                id="spike-protection-processor",
                                include="*",
                                type=ObservabilityPipelineSpikeProtectionProcessorType.SPIKE_PROTECTION,
                                name="MyPartitionedSpikeProtection",
                                spike_action=ObservabilityPipelineSpikeProtectionProcessorSpikeAction.NO_ACTION,
                                partition_fields=[
                                    "service",
                                ],
                                action_when_missing_partitions=ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions.DEFAULT_BUCKET,
                                minimal_threshold_overrides=[
                                    ObservabilityPipelineSpikeProtectionProcessorThresholdOverride(
                                        fields=[
                                            ObservabilityPipelineFieldValue(
                                                name="service",
                                                value="checkout",
                                            ),
                                        ],
                                        minimal_threshold=ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytes(
                                            type=ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType.THRESHOLD,
                                            bytes=53687091200,
                                        ),
                                    ),
                                    ObservabilityPipelineSpikeProtectionProcessorThresholdOverride(
                                        fields=[
                                            ObservabilityPipelineFieldValue(
                                                name="service",
                                                value="payments",
                                            ),
                                        ],
                                        minimal_threshold=ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeep(
                                            type=ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType.ALWAYS_KEEP,
                                        ),
                                    ),
                                ],
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
            name="Pipeline with Spike Protection Threshold Overrides",
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
