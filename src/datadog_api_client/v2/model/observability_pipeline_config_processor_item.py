# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineConfigProcessorItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A processor for the pipeline.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs/metrics should pass through the filter. Logs/metrics that match this query continue to downstream components; others are dropped.
        :type include: str

        :param type: The processor type. The value should always be `filter`.
        :type type: ObservabilityPipelineFilterProcessorType

        :param variables: A list of environment variable mappings to apply to log fields.
        :type variables: [ObservabilityPipelineAddEnvVarsProcessorVariable]

        :param fields: A list of static fields (key-value pairs) that is added to each log event processed by this component.
        :type fields: [ObservabilityPipelineFieldValue]

        :param remaps: Array of VRL remap rules.
        :type remaps: [ObservabilityPipelineCustomProcessorRemap]

        :param action: The action to take on tags with matching keys.
        :type action: ObservabilityPipelineDatadogTagsProcessorAction

        :param keys: A list of tag keys.
        :type keys: [str]

        :param mode: The processing mode.
        :type mode: ObservabilityPipelineDatadogTagsProcessorMode

        :param file: Defines a static enrichment table loaded from a CSV file.
        :type file: ObservabilityPipelineEnrichmentTableFile, optional

        :param geoip: Uses a GeoIP database to enrich logs based on an IP field.
        :type geoip: ObservabilityPipelineEnrichmentTableGeoIp, optional

        :param reference_table: Uses a Datadog reference table to enrich logs.
        :type reference_table: ObservabilityPipelineEnrichmentTableReferenceTable, optional

        :param target: Path where enrichment results should be stored in the log.
        :type target: str

        :param metrics: Configuration for generating individual metrics.
        :type metrics: [ObservabilityPipelineGeneratedMetric], optional

        :param mappings: A list of mapping rules to convert events to the OCSF format.
        :type mappings: [ObservabilityPipelineOcsfMapperProcessorMapping]

        :param disable_library_rules: If set to `true`, disables the default Grok rules provided by Datadog.
        :type disable_library_rules: bool, optional

        :param rules: The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
        :type rules: [ObservabilityPipelineParseGrokProcessorRule]

        :param field: The name of the log field that contains a JSON string.
        :type field: str

        :param always_use_text_key: Whether to always use a text key for element content.
        :type always_use_text_key: bool, optional

        :param attr_prefix: The prefix to use for XML attributes in the parsed output.
        :type attr_prefix: str, optional

        :param include_attr: Whether to include XML attributes in the parsed output.
        :type include_attr: bool, optional

        :param parse_bool: Whether to parse boolean values from strings.
        :type parse_bool: bool, optional

        :param parse_null: Whether to parse null values.
        :type parse_null: bool, optional

        :param parse_number: Whether to parse numeric values from strings.
        :type parse_number: bool, optional

        :param text_key: The key name to use for text content within XML elements. Must be at least 1 character if specified.
        :type text_key: str, optional

        :param drop_events: If set to `true`, logs that match the quota filter and are sent after the quota is exceeded are dropped. Logs that do not match the filter continue through the pipeline. **Note**: You can set either `drop_events` or `overflow_action`, but not both.
        :type drop_events: bool, optional

        :param ignore_when_missing_partitions: If `true`, the processor skips quota checks when partition fields are missing from the logs.
        :type ignore_when_missing_partitions: bool, optional

        :param limit: The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
        :type limit: ObservabilityPipelineQuotaProcessorLimit

        :param name: Name of the quota.
        :type name: str

        :param overflow_action: The action to take when the quota or bucket limit is exceeded. Options:
            - `drop`: Drop the event.
            - `no_action`: Let the event pass through.
            - `overflow_routing`: Route to an overflow destination.
        :type overflow_action: ObservabilityPipelineQuotaProcessorOverflowAction, optional

        :param overrides: A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
        :type overrides: [ObservabilityPipelineQuotaProcessorOverride], optional

        :param partition_fields: A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
        :type partition_fields: [str], optional

        :param too_many_buckets_action: The action to take when the quota or bucket limit is exceeded. Options:
            - `drop`: Drop the event.
            - `no_action`: Let the event pass through.
            - `overflow_routing`: Route to an overflow destination.
        :type too_many_buckets_action: ObservabilityPipelineQuotaProcessorOverflowAction, optional

        :param group_by: A list of fields used to group log events for merging.
        :type group_by: [str]

        :param merge_strategies: List of merge strategies defining how values from grouped events should be combined.
        :type merge_strategies: [ObservabilityPipelineReduceProcessorMergeStrategy]

        :param percentage: The percentage of logs to sample.
        :type percentage: float

        :param arrays: A list of array split configurations.
        :type arrays: [ObservabilityPipelineSplitArrayProcessorArrayConfig]

        :param threshold: the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
        :type threshold: int

        :param window: The time window in seconds over which the threshold applies.
        :type window: float
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.observability_pipeline_filter_processor import (
            ObservabilityPipelineFilterProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor import (
            ObservabilityPipelineAddEnvVarsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_add_fields_processor import (
            ObservabilityPipelineAddFieldsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_add_hostname_processor import (
            ObservabilityPipelineAddHostnameProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_custom_processor import (
            ObservabilityPipelineCustomProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor import (
            ObservabilityPipelineDatadogTagsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_dedupe_processor import (
            ObservabilityPipelineDedupeProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor import (
            ObservabilityPipelineEnrichmentTableProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_generate_metrics_processor import (
            ObservabilityPipelineGenerateMetricsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor import (
            ObservabilityPipelineOcsfMapperProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor import (
            ObservabilityPipelineParseGrokProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_json_processor import (
            ObservabilityPipelineParseJSONProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_xml_processor import (
            ObservabilityPipelineParseXMLProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_quota_processor import (
            ObservabilityPipelineQuotaProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_reduce_processor import (
            ObservabilityPipelineReduceProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor import (
            ObservabilityPipelineRemoveFieldsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor import (
            ObservabilityPipelineRenameFieldsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_sample_processor import (
            ObservabilityPipelineSampleProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor import (
            ObservabilityPipelineSensitiveDataScannerProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_split_array_processor import (
            ObservabilityPipelineSplitArrayProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_throttle_processor import (
            ObservabilityPipelineThrottleProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor import (
            ObservabilityPipelineMetricTagsProcessor,
        )

        return {
            "oneOf": [
                ObservabilityPipelineFilterProcessor,
                ObservabilityPipelineAddEnvVarsProcessor,
                ObservabilityPipelineAddFieldsProcessor,
                ObservabilityPipelineAddHostnameProcessor,
                ObservabilityPipelineCustomProcessor,
                ObservabilityPipelineDatadogTagsProcessor,
                ObservabilityPipelineDedupeProcessor,
                ObservabilityPipelineEnrichmentTableProcessor,
                ObservabilityPipelineGenerateMetricsProcessor,
                ObservabilityPipelineOcsfMapperProcessor,
                ObservabilityPipelineParseGrokProcessor,
                ObservabilityPipelineParseJSONProcessor,
                ObservabilityPipelineParseXMLProcessor,
                ObservabilityPipelineQuotaProcessor,
                ObservabilityPipelineReduceProcessor,
                ObservabilityPipelineRemoveFieldsProcessor,
                ObservabilityPipelineRenameFieldsProcessor,
                ObservabilityPipelineSampleProcessor,
                ObservabilityPipelineSensitiveDataScannerProcessor,
                ObservabilityPipelineSplitArrayProcessor,
                ObservabilityPipelineThrottleProcessor,
                ObservabilityPipelineMetricTagsProcessor,
            ],
        }
