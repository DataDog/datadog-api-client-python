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

        :param encoding: The output encoding format.
        :type encoding: ObservabilityPipelineSumoLogicDestinationEncoding, optional

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

        :param bulk_index: The index or datastream to write logs to in Elasticsearch.
        :type bulk_index: str, optional

        :param keepalive: Optional socket keepalive duration in milliseconds.
        :type keepalive: int, optional

        :param tls: Configuration for enabling TLS encryption.
        :type tls: ObservabilityPipelineTls, optional

        :param blob_prefix: Optional prefix for blobs written to the container.
        :type blob_prefix: str, optional

        :param container_name: The name of the Azure Blob Storage container to store logs in.
        :type container_name: str

        :param client_id: Azure AD client ID used for authentication.
        :type client_id: str

        :param dcr_immutable_id: The immutable ID of the Data Collection Rule (DCR).
        :type dcr_immutable_id: str

        :param table: The name of the Log Analytics table where logs will be sent.
        :type table: str

        :param tenant_id: Azure AD tenant ID.
        :type tenant_id: str
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

        return {
            "oneOf": [
                ObservabilityPipelineDatadogLogsDestination,
                ObservabilityPipelineSumoLogicDestination,
                ObservabilityPipelineElasticsearchDestination,
                ObservabilityPipelineRsyslogDestination,
                ObservabilityPipelineSyslogNgDestination,
                AzureStorageDestination,
                MicrosoftSentinelDestination,
            ],
        }
