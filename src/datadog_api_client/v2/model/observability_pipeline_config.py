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
    from datadog_api_client.v2.model.observability_pipeline_config_pipeline_type import (
        ObservabilityPipelineConfigPipelineType,
    )
    from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
        ObservabilityPipelineConfigProcessorGroup,
    )
    from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
        ObservabilityPipelineConfigSourceItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_client_destination import (
        ObservabilityPipelineHttpClientDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination import (
        ObservabilityPipelineAmazonOpenSearchDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination import (
        ObservabilityPipelineAmazonS3Destination,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_security_lake_destination import (
        ObservabilityPipelineAmazonSecurityLakeDestination,
    )
    from datadog_api_client.v2.model.azure_storage_destination import AzureStorageDestination
    from datadog_api_client.v2.model.observability_pipeline_cloud_prem_destination import (
        ObservabilityPipelineCloudPremDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination import (
        ObservabilityPipelineCrowdStrikeNextGenSiemDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
        ObservabilityPipelineDatadogLogsDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination import (
        ObservabilityPipelineElasticsearchDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_chronicle_destination import (
        ObservabilityPipelineGoogleChronicleDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination import (
        ObservabilityPipelineGoogleCloudStorageDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_destination import (
        ObservabilityPipelineGooglePubSubDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_destination import (
        ObservabilityPipelineKafkaDestination,
    )
    from datadog_api_client.v2.model.microsoft_sentinel_destination import MicrosoftSentinelDestination
    from datadog_api_client.v2.model.observability_pipeline_new_relic_destination import (
        ObservabilityPipelineNewRelicDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_open_search_destination import (
        ObservabilityPipelineOpenSearchDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_rsyslog_destination import (
        ObservabilityPipelineRsyslogDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination import (
        ObservabilityPipelineSentinelOneDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_destination import (
        ObservabilityPipelineSocketDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_destination import (
        ObservabilityPipelineSplunkHecDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination import (
        ObservabilityPipelineSumoLogicDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_syslog_ng_destination import (
        ObservabilityPipelineSyslogNgDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_metrics_destination import (
        ObservabilityPipelineDatadogMetricsDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
        ObservabilityPipelineDatadogAgentSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_data_firehose_source import (
        ObservabilityPipelineAmazonDataFirehoseSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_source import ObservabilityPipelineAmazonS3Source
    from datadog_api_client.v2.model.observability_pipeline_fluent_bit_source import (
        ObservabilityPipelineFluentBitSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_fluentd_source import ObservabilityPipelineFluentdSource
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_source import (
        ObservabilityPipelineGooglePubSubSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_client_source import (
        ObservabilityPipelineHttpClientSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_server_source import (
        ObservabilityPipelineHttpServerSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_source import ObservabilityPipelineKafkaSource
    from datadog_api_client.v2.model.observability_pipeline_logstash_source import ObservabilityPipelineLogstashSource
    from datadog_api_client.v2.model.observability_pipeline_rsyslog_source import ObservabilityPipelineRsyslogSource
    from datadog_api_client.v2.model.observability_pipeline_socket_source import ObservabilityPipelineSocketSource
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_source import (
        ObservabilityPipelineSplunkHecSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_splunk_tcp_source import (
        ObservabilityPipelineSplunkTcpSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_source import (
        ObservabilityPipelineSumoLogicSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_syslog_ng_source import ObservabilityPipelineSyslogNgSource
    from datadog_api_client.v2.model.observability_pipeline_opentelemetry_source import (
        ObservabilityPipelineOpentelemetrySource,
    )


class ObservabilityPipelineConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_config_destination_item import (
            ObservabilityPipelineConfigDestinationItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_pipeline_type import (
            ObservabilityPipelineConfigPipelineType,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
            ObservabilityPipelineConfigProcessorGroup,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
            ObservabilityPipelineConfigSourceItem,
        )

        return {
            "destinations": ([ObservabilityPipelineConfigDestinationItem],),
            "pipeline_type": (ObservabilityPipelineConfigPipelineType,),
            "processor_groups": ([ObservabilityPipelineConfigProcessorGroup],),
            "processors": ([ObservabilityPipelineConfigProcessorGroup],),
            "sources": ([ObservabilityPipelineConfigSourceItem],),
            "use_legacy_search_syntax": (bool,),
        }

    attribute_map = {
        "destinations": "destinations",
        "pipeline_type": "pipeline_type",
        "processor_groups": "processor_groups",
        "processors": "processors",
        "sources": "sources",
        "use_legacy_search_syntax": "use_legacy_search_syntax",
    }

    def __init__(
        self_,
        destinations: List[
            Union[
                ObservabilityPipelineConfigDestinationItem,
                ObservabilityPipelineHttpClientDestination,
                ObservabilityPipelineAmazonOpenSearchDestination,
                ObservabilityPipelineAmazonS3Destination,
                ObservabilityPipelineAmazonSecurityLakeDestination,
                AzureStorageDestination,
                ObservabilityPipelineCloudPremDestination,
                ObservabilityPipelineCrowdStrikeNextGenSiemDestination,
                ObservabilityPipelineDatadogLogsDestination,
                ObservabilityPipelineElasticsearchDestination,
                ObservabilityPipelineGoogleChronicleDestination,
                ObservabilityPipelineGoogleCloudStorageDestination,
                ObservabilityPipelineGooglePubSubDestination,
                ObservabilityPipelineKafkaDestination,
                MicrosoftSentinelDestination,
                ObservabilityPipelineNewRelicDestination,
                ObservabilityPipelineOpenSearchDestination,
                ObservabilityPipelineRsyslogDestination,
                ObservabilityPipelineSentinelOneDestination,
                ObservabilityPipelineSocketDestination,
                ObservabilityPipelineSplunkHecDestination,
                ObservabilityPipelineSumoLogicDestination,
                ObservabilityPipelineSyslogNgDestination,
                ObservabilityPipelineDatadogMetricsDestination,
            ]
        ],
        sources: List[
            Union[
                ObservabilityPipelineConfigSourceItem,
                ObservabilityPipelineDatadogAgentSource,
                ObservabilityPipelineAmazonDataFirehoseSource,
                ObservabilityPipelineAmazonS3Source,
                ObservabilityPipelineFluentBitSource,
                ObservabilityPipelineFluentdSource,
                ObservabilityPipelineGooglePubSubSource,
                ObservabilityPipelineHttpClientSource,
                ObservabilityPipelineHttpServerSource,
                ObservabilityPipelineKafkaSource,
                ObservabilityPipelineLogstashSource,
                ObservabilityPipelineRsyslogSource,
                ObservabilityPipelineSocketSource,
                ObservabilityPipelineSplunkHecSource,
                ObservabilityPipelineSplunkTcpSource,
                ObservabilityPipelineSumoLogicSource,
                ObservabilityPipelineSyslogNgSource,
                ObservabilityPipelineOpentelemetrySource,
            ]
        ],
        pipeline_type: Union[ObservabilityPipelineConfigPipelineType, UnsetType] = unset,
        processor_groups: Union[List[ObservabilityPipelineConfigProcessorGroup], UnsetType] = unset,
        processors: Union[List[ObservabilityPipelineConfigProcessorGroup], UnsetType] = unset,
        use_legacy_search_syntax: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Specifies the pipeline's configuration, including its sources, processors, and destinations.

        :param destinations: A list of destination components where processed logs are sent.
        :type destinations: [ObservabilityPipelineConfigDestinationItem]

        :param pipeline_type: The type of data being ingested. Defaults to ``logs`` if not specified.
        :type pipeline_type: ObservabilityPipelineConfigPipelineType, optional

        :param processor_groups: A list of processor groups that transform or enrich log data.
        :type processor_groups: [ObservabilityPipelineConfigProcessorGroup], optional

        :param processors: A list of processor groups that transform or enrich log data.

            **Deprecated:** This field is deprecated, you should now use the processor_groups field. **Deprecated**.
        :type processors: [ObservabilityPipelineConfigProcessorGroup], optional

        :param sources: A list of configured data sources for the pipeline.
        :type sources: [ObservabilityPipelineConfigSourceItem]

        :param use_legacy_search_syntax: Set to ``true`` to continue using the legacy search syntax while migrating filter queries. After migrating all queries to the new syntax, set to ``false``.
            The legacy syntax is deprecated and will eventually be removed.
            Requires Observability Pipelines Worker 2.11 or later.
            See `Upgrade Your Filter Queries to the New Search Syntax <https://docs.datadoghq.com/observability_pipelines/guide/upgrade_your_filter_queries_to_the_new_search_syntax/>`_ for more information.
        :type use_legacy_search_syntax: bool, optional
        """
        if pipeline_type is not unset:
            kwargs["pipeline_type"] = pipeline_type
        if processor_groups is not unset:
            kwargs["processor_groups"] = processor_groups
        if processors is not unset:
            kwargs["processors"] = processors
        if use_legacy_search_syntax is not unset:
            kwargs["use_legacy_search_syntax"] = use_legacy_search_syntax
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.sources = sources
