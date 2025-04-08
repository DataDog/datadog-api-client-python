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

        return {
            "oneOf": [
                ObservabilityPipelineKafkaSource,
                ObservabilityPipelineDatadogAgentSource,
            ],
        }
