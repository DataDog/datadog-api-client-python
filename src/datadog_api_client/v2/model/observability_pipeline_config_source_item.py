# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineConfigSourceItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A data source for the pipeline.

        :param group_id: Consumer group ID used by the Kafka client.
        :type group_id: str

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param librdkafka_options: Optional list of advanced Kafka client configuration options, defined as key-value pairs.
        :type librdkafka_options: [ObservabilityPipelineKafkaSourceLibrdkafkaOption], optional

        :param sasl: Specifies the SASL mechanism for authenticating with a Kafka cluster.
        :type sasl: ObservabilityPipelineKafkaSourceSasl, optional

        :param tls: Configuration for enabling TLS encryption.
        :type tls: ObservabilityPipelineTls, optional

        :param topics: A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
        :type topics: [str]

        :param type: The source type. The value should always be `kafka`.
        :type type: ObservabilityPipelineKafkaSourceType

        :param auth: AWS authentication credentials used for accessing AWS services such as S3.
            If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).

        :type auth: ObservabilityPipelineAwsAuth, optional

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param project: The GCP project ID that owns the Pub/Sub subscription.
        :type project: str

        :param subscription: The Pub/Sub subscription name from which messages are consumed.
        :type subscription: str

        :param auth_strategy: Optional authentication strategy for HTTP requests.
        :type auth_strategy: ObservabilityPipelineHttpClientSourceAuthStrategy, optional

        :param scrape_interval_secs: The interval (in seconds) between HTTP scrape requests.
        :type scrape_interval_secs: int, optional

        :param scrape_timeout_secs: The timeout (in seconds) for each scrape request.
        :type scrape_timeout_secs: int, optional
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
        from datadog_api_client.v2.model.observability_pipeline_kafka_source import ObservabilityPipelineKafkaSource
        from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
            ObservabilityPipelineDatadogAgentSource,
        )
        from datadog_api_client.v2.model.observability_pipeline_amazon_data_firehose_source import (
            ObservabilityPipelineAmazonDataFirehoseSource,
        )
        from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_source import (
            ObservabilityPipelineGooglePubSubSource,
        )
        from datadog_api_client.v2.model.observability_pipeline_http_client_source import (
            ObservabilityPipelineHttpClientSource,
        )
        from datadog_api_client.v2.model.observability_pipeline_logstash_source import (
            ObservabilityPipelineLogstashSource,
        )

        return {
            "oneOf": [
                ObservabilityPipelineKafkaSource,
                ObservabilityPipelineDatadogAgentSource,
                ObservabilityPipelineAmazonDataFirehoseSource,
                ObservabilityPipelineGooglePubSubSource,
                ObservabilityPipelineHttpClientSource,
                ObservabilityPipelineLogstashSource,
            ],
        }
