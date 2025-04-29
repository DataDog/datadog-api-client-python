# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_config_destination_item import (
        ObservabilityPipelineConfigDestinationItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_config_processor_item import (
        ObservabilityPipelineConfigProcessorItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
        ObservabilityPipelineConfigSourceItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
        ObservabilityPipelineDatadogLogsDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination import (
        ObservabilityPipelineAmazonS3Destination,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination import (
        ObservabilityPipelineGoogleCloudStorageDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_destination import (
        ObservabilityPipelineSplunkHecDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination import (
        ObservabilityPipelineSumoLogicDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination import (
        ObservabilityPipelineElasticsearchDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_rsyslog_destination import (
        ObservabilityPipelineRsyslogDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_syslog_ng_destination import (
        ObservabilityPipelineSyslogNgDestination,
    )
    from datadog_api_client.v2.model.azure_storage_destination import AzureStorageDestination
    from datadog_api_client.v2.model.microsoft_sentinel_destination import MicrosoftSentinelDestination
    from datadog_api_client.v2.model.observability_pipeline_google_chronicle_destination import (
        ObservabilityPipelineGoogleChronicleDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_new_relic_destination import (
        ObservabilityPipelineNewRelicDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination import (
        ObservabilityPipelineSentinelOneDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_open_search_destination import (
        ObservabilityPipelineOpenSearchDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination import (
        ObservabilityPipelineAmazonOpenSearchDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
    from datadog_api_client.v2.model.observability_pipeline_parse_json_processor import (
        ObservabilityPipelineParseJSONProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_quota_processor import ObservabilityPipelineQuotaProcessor
    from datadog_api_client.v2.model.observability_pipeline_add_fields_processor import (
        ObservabilityPipelineAddFieldsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor import (
        ObservabilityPipelineRemoveFieldsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor import (
        ObservabilityPipelineRenameFieldsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_generate_metrics_processor import (
        ObservabilityPipelineGenerateMetricsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_sample_processor import ObservabilityPipelineSampleProcessor
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor import (
        ObservabilityPipelineParseGrokProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor import (
        ObservabilityPipelineSensitiveDataScannerProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor import (
        ObservabilityPipelineOcsfMapperProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor import (
        ObservabilityPipelineAddEnvVarsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_dedupe_processor import ObservabilityPipelineDedupeProcessor
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor import (
        ObservabilityPipelineEnrichmentTableProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_reduce_processor import ObservabilityPipelineReduceProcessor
    from datadog_api_client.v2.model.observability_pipeline_throttle_processor import (
        ObservabilityPipelineThrottleProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_source import ObservabilityPipelineKafkaSource
    from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
        ObservabilityPipelineDatadogAgentSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_splunk_tcp_source import (
        ObservabilityPipelineSplunkTcpSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_source import (
        ObservabilityPipelineSplunkHecSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_source import ObservabilityPipelineAmazonS3Source
    from datadog_api_client.v2.model.observability_pipeline_fluentd_source import ObservabilityPipelineFluentdSource
    from datadog_api_client.v2.model.observability_pipeline_fluent_bit_source import (
        ObservabilityPipelineFluentBitSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_server_source import (
        ObservabilityPipelineHttpServerSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_source import (
        ObservabilityPipelineSumoLogicSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_rsyslog_source import ObservabilityPipelineRsyslogSource
    from datadog_api_client.v2.model.observability_pipeline_syslog_ng_source import ObservabilityPipelineSyslogNgSource
    from datadog_api_client.v2.model.observability_pipeline_amazon_data_firehose_source import (
        ObservabilityPipelineAmazonDataFirehoseSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_source import (
        ObservabilityPipelineGooglePubSubSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_client_source import (
        ObservabilityPipelineHttpClientSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_logstash_source import ObservabilityPipelineLogstashSource


class ObservabilityPipelineConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_config_destination_item import (
            ObservabilityPipelineConfigDestinationItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_processor_item import (
            ObservabilityPipelineConfigProcessorItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
            ObservabilityPipelineConfigSourceItem,
        )

        return {
            "destinations": ([ObservabilityPipelineConfigDestinationItem],),
            "processors": ([ObservabilityPipelineConfigProcessorItem],),
            "sources": ([ObservabilityPipelineConfigSourceItem],),
        }

    attribute_map = {
        "destinations": "destinations",
        "processors": "processors",
        "sources": "sources",
    }

    def __init__(
        self_,
        destinations: List[
            Union[
                ObservabilityPipelineConfigDestinationItem,
                ObservabilityPipelineDatadogLogsDestination,
                ObservabilityPipelineAmazonS3Destination,
                ObservabilityPipelineGoogleCloudStorageDestination,
                ObservabilityPipelineSplunkHecDestination,
                ObservabilityPipelineSumoLogicDestination,
                ObservabilityPipelineElasticsearchDestination,
                ObservabilityPipelineRsyslogDestination,
                ObservabilityPipelineSyslogNgDestination,
                AzureStorageDestination,
                MicrosoftSentinelDestination,
                ObservabilityPipelineGoogleChronicleDestination,
                ObservabilityPipelineNewRelicDestination,
                ObservabilityPipelineSentinelOneDestination,
                ObservabilityPipelineOpenSearchDestination,
                ObservabilityPipelineAmazonOpenSearchDestination,
            ]
        ],
        sources: List[
            Union[
                ObservabilityPipelineConfigSourceItem,
                ObservabilityPipelineKafkaSource,
                ObservabilityPipelineDatadogAgentSource,
                ObservabilityPipelineSplunkTcpSource,
                ObservabilityPipelineSplunkHecSource,
                ObservabilityPipelineAmazonS3Source,
                ObservabilityPipelineFluentdSource,
                ObservabilityPipelineFluentBitSource,
                ObservabilityPipelineHttpServerSource,
                ObservabilityPipelineSumoLogicSource,
                ObservabilityPipelineRsyslogSource,
                ObservabilityPipelineSyslogNgSource,
                ObservabilityPipelineAmazonDataFirehoseSource,
                ObservabilityPipelineGooglePubSubSource,
                ObservabilityPipelineHttpClientSource,
                ObservabilityPipelineLogstashSource,
            ]
        ],
        processors: Union[
            List[
                Union[
                    ObservabilityPipelineConfigProcessorItem,
                    ObservabilityPipelineFilterProcessor,
                    ObservabilityPipelineParseJSONProcessor,
                    ObservabilityPipelineQuotaProcessor,
                    ObservabilityPipelineAddFieldsProcessor,
                    ObservabilityPipelineRemoveFieldsProcessor,
                    ObservabilityPipelineRenameFieldsProcessor,
                    ObservabilityPipelineGenerateMetricsProcessor,
                    ObservabilityPipelineSampleProcessor,
                    ObservabilityPipelineParseGrokProcessor,
                    ObservabilityPipelineSensitiveDataScannerProcessor,
                    ObservabilityPipelineOcsfMapperProcessor,
                    ObservabilityPipelineAddEnvVarsProcessor,
                    ObservabilityPipelineDedupeProcessor,
                    ObservabilityPipelineEnrichmentTableProcessor,
                    ObservabilityPipelineReduceProcessor,
                    ObservabilityPipelineThrottleProcessor,
                ]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Specifies the pipeline's configuration, including its sources, processors, and destinations.

        :param destinations: A list of destination components where processed logs are sent.
        :type destinations: [ObservabilityPipelineConfigDestinationItem]

        :param processors: A list of processors that transform or enrich log data.
        :type processors: [ObservabilityPipelineConfigProcessorItem], optional

        :param sources: A list of configured data sources for the pipeline.
        :type sources: [ObservabilityPipelineConfigSourceItem]
        """
        if processors is not unset:
            kwargs["processors"] = processors
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.sources = sources
