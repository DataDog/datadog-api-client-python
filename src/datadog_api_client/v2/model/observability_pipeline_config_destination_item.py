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
        :type key_prefix: str, none_type, optional

        :param region: AWS region of the S3 bucket.
        :type region: str

        :param storage_class: S3 storage class.
        :type storage_class: ObservabilityPipelineAmazonS3DestinationStorageClass

        :param tls: Configuration for enabling TLS encryption.
        :type tls: ObservabilityPipelineTls, optional

        :param acl: Access control list setting for objects written to the bucket.
        :type acl: ObservabilityPipelineGoogleCloudStorageDestinationAcl

        :param metadata: Custom metadata key-value pairs added to each object.
        :type metadata: [ObservabilityPipelineMetadataEntry]

        :param auto_extract_timestamp: If `true`, Splunk tries to extract timestamps from incoming log events.
            If `false`, Splunk assigns the time the event was received.

        :type auto_extract_timestamp: bool, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineSplunkHecDestinationEncoding, optional

        :param index: Optional name of the Splunk index where logs are written.
        :type index: str, optional

        :param sourcetype: The Splunk sourcetype to assign to log events.
        :type sourcetype: str, optional
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

        return {
            "oneOf": [
                ObservabilityPipelineDatadogLogsDestination,
                ObservabilityPipelineAmazonS3Destination,
                ObservabilityPipelineGoogleCloudStorageDestination,
                ObservabilityPipelineSplunkHecDestination,
            ],
        }
