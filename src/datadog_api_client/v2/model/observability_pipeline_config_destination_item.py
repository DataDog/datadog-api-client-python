# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineConfigDestinationItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A destination for the pipeline.

        :param auth_strategy: HTTP authentication strategy.
        :type auth_strategy: ObservabilityPipelineHttpClientDestinationAuthStrategy, optional

        :param compression: Compression configuration for HTTP requests.
        :type compression: ObservabilityPipelineHttpClientDestinationCompression, optional

        :param custom_key: Name of the environment variable or secret that holds a custom header value (used with custom auth strategies).
        :type custom_key: str, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineHttpClientDestinationEncoding

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the input for this component.
        :type inputs: [str]

        :param password_key: Name of the environment variable or secret that holds the password (used when `auth_strategy` is `basic`).
        :type password_key: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param token_key: Name of the environment variable or secret that holds the bearer token (used when `auth_strategy` is `bearer`).
        :type token_key: str, optional

        :param type: The destination type. The value should always be `http_client`.
        :type type: ObservabilityPipelineHttpClientDestinationType

        :param uri_key: Name of the environment variable or secret that holds the HTTP endpoint URI.
        :type uri_key: str, optional

        :param username_key: Name of the environment variable or secret that holds the username (used when `auth_strategy` is `basic`).
        :type username_key: str, optional

        :param auth: Authentication settings for the Amazon OpenSearch destination.
            The `strategy` field determines whether basic or AWS-based authentication is used.
        :type auth: ObservabilityPipelineAmazonOpenSearchDestinationAuth

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param bulk_index: The index to write logs to.
        :type bulk_index: str, optional

        :param bucket: S3 bucket name.
        :type bucket: str

        :param key_prefix: Optional prefix for object keys.
        :type key_prefix: str, optional

        :param region: AWS region of the S3 bucket.
        :type region: str

        :param storage_class: S3 storage class.
        :type storage_class: ObservabilityPipelineAmazonS3DestinationStorageClass

        :param custom_source_name: Custom source name for the logs in Security Lake.
        :type custom_source_name: str

        :param blob_prefix: Optional prefix for blobs written to the container.
        :type blob_prefix: str, optional

        :param connection_string_key: Name of the environment variable or secret that holds the Azure Storage connection string.
        :type connection_string_key: str, optional

        :param container_name: The name of the Azure Blob Storage container to store logs in.
        :type container_name: str

        :param endpoint_url_key: Name of the environment variable or secret that holds the CloudPrem endpoint URL.
        :type endpoint_url_key: str, optional

        :param routes: A list of routing rules that forward matching logs to Datadog using dedicated API keys.
        :type routes: [ObservabilityPipelineDatadogLogsDestinationRoute], optional

        :param api_version: The Elasticsearch API version to use. Set to `auto` to auto-detect.
        :type api_version: ObservabilityPipelineElasticsearchDestinationApiVersion, optional

        :param data_stream: Configuration options for writing to Elasticsearch Data Streams instead of a fixed index.
        :type data_stream: ObservabilityPipelineElasticsearchDestinationDataStream, optional

        :param customer_id: The Google Chronicle customer ID.
        :type customer_id: str

        :param log_type: The log type metadata associated with the Chronicle destination.
        :type log_type: str, optional

        :param acl: Access control list setting for objects written to the bucket.
        :type acl: ObservabilityPipelineGoogleCloudStorageDestinationAcl, optional

        :param metadata: Custom metadata to attach to each object uploaded to the GCS bucket.
        :type metadata: [ObservabilityPipelineMetadataEntry], optional

        :param project: The Google Cloud project ID that owns the Pub/Sub topic.
        :type project: str

        :param topic: The Pub/Sub topic name to publish logs to.
        :type topic: str

        :param bootstrap_servers_key: Name of the environment variable or secret that holds the Kafka bootstrap servers list.
        :type bootstrap_servers_key: str, optional

        :param headers_key: The field name to use for Kafka message headers.
        :type headers_key: str, optional

        :param key_field: The field name to use as the Kafka message key.
        :type key_field: str, optional

        :param librdkafka_options: Optional list of advanced Kafka producer configuration options, defined as key-value pairs.
        :type librdkafka_options: [ObservabilityPipelineKafkaLibrdkafkaOption], optional

        :param message_timeout_ms: Maximum time in milliseconds to wait for message delivery confirmation.
        :type message_timeout_ms: int, optional

        :param rate_limit_duration_secs: Duration in seconds for the rate limit window.
        :type rate_limit_duration_secs: int, optional

        :param rate_limit_num: Maximum number of messages allowed per rate limit duration.
        :type rate_limit_num: int, optional

        :param sasl: Specifies the SASL mechanism for authenticating with a Kafka cluster.
        :type sasl: ObservabilityPipelineKafkaSasl, optional

        :param socket_timeout_ms: Socket timeout in milliseconds for network requests.
        :type socket_timeout_ms: int, optional

        :param client_id: Azure AD client ID used for authentication.
        :type client_id: str

        :param client_secret_key: Name of the environment variable or secret that holds the Azure AD client secret.
        :type client_secret_key: str, optional

        :param dce_uri_key: Name of the environment variable or secret that holds the Data Collection Endpoint (DCE) URI.
        :type dce_uri_key: str, optional

        :param dcr_immutable_id: The immutable ID of the Data Collection Rule (DCR).
        :type dcr_immutable_id: str

        :param table: The name of the Log Analytics table where logs are sent.
        :type table: str

        :param tenant_id: Azure AD tenant ID.
        :type tenant_id: str

        :param account_id_key: Name of the environment variable or secret that holds the New Relic account ID.
        :type account_id_key: str, optional

        :param license_key_key: Name of the environment variable or secret that holds the New Relic license key.
        :type license_key_key: str, optional

        :param keepalive: Optional socket keepalive duration in milliseconds.
        :type keepalive: int, optional

        :param address_key: Name of the environment variable or secret that holds the socket address (host:port).
        :type address_key: str, optional

        :param framing: Framing method configuration.
        :type framing: ObservabilityPipelineSocketDestinationFraming

        :param mode: Protocol used to send logs.
        :type mode: ObservabilityPipelineSocketDestinationMode

        :param auto_extract_timestamp: If `true`, Splunk tries to extract timestamps from incoming log events.
            If `false`, Splunk assigns the time the event was received.
        :type auto_extract_timestamp: bool, optional

        :param index: Optional name of the Splunk index where logs are written.
        :type index: str, optional

        :param sourcetype: The Splunk sourcetype to assign to log events.
        :type sourcetype: str, optional

        :param header_custom_fields: A list of custom headers to include in the request to Sumo Logic.
        :type header_custom_fields: [ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem], optional

        :param header_host_name: Optional override for the host name header.
        :type header_host_name: str, optional

        :param header_source_category: Optional override for the source category header.
        :type header_source_category: str, optional

        :param header_source_name: Optional override for the source name header.
        :type header_source_name: str, optional
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

        return {
            "oneOf": [
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
            ],
        }
