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
    from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
        ObservabilityPipelineConfigProcessorGroup,
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
    from datadog_api_client.v2.model.observability_pipeline_socket_destination import (
        ObservabilityPipelineSocketDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_security_lake_destination import (
        ObservabilityPipelineAmazonSecurityLakeDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination import (
        ObservabilityPipelineCrowdStrikeNextGenSiemDestination,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_destination import (
        ObservabilityPipelineGooglePubSubDestination,
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
    from datadog_api_client.v2.model.observability_pipeline_socket_source import ObservabilityPipelineSocketSource


class ObservabilityPipelineConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_config_destination_item import (
            ObservabilityPipelineConfigDestinationItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_processor_group import (
            ObservabilityPipelineConfigProcessorGroup,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
            ObservabilityPipelineConfigSourceItem,
        )

        return {
            "destinations": ([ObservabilityPipelineConfigDestinationItem],),
            "processors": ([ObservabilityPipelineConfigProcessorGroup],),
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
                ObservabilityPipelineSocketDestination,
                ObservabilityPipelineAmazonSecurityLakeDestination,
                ObservabilityPipelineCrowdStrikeNextGenSiemDestination,
                ObservabilityPipelineGooglePubSubDestination,
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
                ObservabilityPipelineSocketSource,
            ]
        ],
        processors: Union[List[ObservabilityPipelineConfigProcessorGroup], UnsetType] = unset,
        **kwargs,
    ):
        """
        Specifies the pipeline's configuration, including its sources, processors, and destinations.

        :param destinations: A list of destination components where processed logs are sent.
        :type destinations: [ObservabilityPipelineConfigDestinationItem]

        :param processors: A list of processor groups that transform or enrich log data.
        :type processors: [ObservabilityPipelineConfigProcessorGroup], optional

        :param sources: A list of configured data sources for the pipeline.
        :type sources: [ObservabilityPipelineConfigSourceItem]
        """
        if processors is not unset:
            kwargs["processors"] = processors
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.sources = sources
