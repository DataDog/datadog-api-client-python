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

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the `input` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be `datadog_logs`.
        :type type: ObservabilityPipelineDatadogLogsDestinationType

        :param auth: AWS authentication credentials used for accessing AWS services such as S3.
            If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).

        :type auth: ObservabilityPipelineAwsAuth, optional

        :param bucket: S3 bucket name.
        :type bucket: str

        :param key_prefix: Optional prefix for object keys.
        :type key_prefix: str, optional

        :param region: AWS region of the S3 bucket.
        :type region: str

        :param storage_class: S3 storage class.
        :type storage_class: ObservabilityPipelineAmazonS3DestinationStorageClass

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param acl: Access control list setting for objects written to the bucket.
        :type acl: ObservabilityPipelineGoogleCloudStorageDestinationAcl

        :param metadata: Custom metadata to attach to each object uploaded to the GCS bucket.
        :type metadata: [ObservabilityPipelineMetadataEntry], optional

        :param auto_extract_timestamp: If `true`, Splunk tries to extract timestamps from incoming log events.
            If `false`, Splunk assigns the time the event was received.

        :type auto_extract_timestamp: bool, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineSplunkHecDestinationEncoding, optional

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

        :param api_version: The Elasticsearch API version to use. Set to `auto` to auto-detect.
        :type api_version: ObservabilityPipelineElasticsearchDestinationApiVersion, optional

        :param bulk_index: The index to write logs to in Elasticsearch.
        :type bulk_index: str, optional

        :param keepalive: Optional socket keepalive duration in milliseconds.
        :type keepalive: int, optional

        :param blob_prefix: Optional prefix for blobs written to the container.
        :type blob_prefix: str, optional

        :param container_name: The name of the Azure Blob Storage container to store logs in.
        :type container_name: str

        :param client_id: Azure AD client ID used for authentication.
        :type client_id: str

        :param dcr_immutable_id: The immutable ID of the Data Collection Rule (DCR).
        :type dcr_immutable_id: str

        :param table: The name of the Log Analytics table where logs are sent.
        :type table: str

        :param tenant_id: Azure AD tenant ID.
        :type tenant_id: str

        :param customer_id: The Google Chronicle customer ID.
        :type customer_id: str

        :param log_type: The log type metadata associated with the Chronicle destination.
        :type log_type: str, optional
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

        return {
            "oneOf": [
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
            ],
        }
