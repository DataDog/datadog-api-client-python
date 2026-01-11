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
    from datadog_api_client.v2.model.observability_pipeline_kafka_destination_compression import (
        ObservabilityPipelineKafkaDestinationCompression,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_destination_encoding import (
        ObservabilityPipelineKafkaDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_librdkafka_option import (
        ObservabilityPipelineKafkaLibrdkafkaOption,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_sasl import ObservabilityPipelineKafkaSasl
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_kafka_destination_type import (
        ObservabilityPipelineKafkaDestinationType,
    )


class ObservabilityPipelineKafkaDestination(ModelNormal):
    validations = {
        "message_timeout_ms": {
            "inclusive_minimum": 1,
        },
        "rate_limit_duration_secs": {
            "inclusive_minimum": 1,
        },
        "rate_limit_num": {
            "inclusive_minimum": 1,
        },
        "socket_timeout_ms": {
            "inclusive_maximum": 300000,
            "inclusive_minimum": 10,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_kafka_destination_compression import (
            ObservabilityPipelineKafkaDestinationCompression,
        )
        from datadog_api_client.v2.model.observability_pipeline_kafka_destination_encoding import (
            ObservabilityPipelineKafkaDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_kafka_librdkafka_option import (
            ObservabilityPipelineKafkaLibrdkafkaOption,
        )
        from datadog_api_client.v2.model.observability_pipeline_kafka_sasl import ObservabilityPipelineKafkaSasl
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_kafka_destination_type import (
            ObservabilityPipelineKafkaDestinationType,
        )

        return {
            "compression": (ObservabilityPipelineKafkaDestinationCompression,),
            "encoding": (ObservabilityPipelineKafkaDestinationEncoding,),
            "headers_key": (str,),
            "id": (str,),
            "inputs": ([str],),
            "key_field": (str,),
            "librdkafka_options": ([ObservabilityPipelineKafkaLibrdkafkaOption],),
            "message_timeout_ms": (int,),
            "rate_limit_duration_secs": (int,),
            "rate_limit_num": (int,),
            "sasl": (ObservabilityPipelineKafkaSasl,),
            "socket_timeout_ms": (int,),
            "tls": (ObservabilityPipelineTls,),
            "topic": (str,),
            "type": (ObservabilityPipelineKafkaDestinationType,),
        }

    attribute_map = {
        "compression": "compression",
        "encoding": "encoding",
        "headers_key": "headers_key",
        "id": "id",
        "inputs": "inputs",
        "key_field": "key_field",
        "librdkafka_options": "librdkafka_options",
        "message_timeout_ms": "message_timeout_ms",
        "rate_limit_duration_secs": "rate_limit_duration_secs",
        "rate_limit_num": "rate_limit_num",
        "sasl": "sasl",
        "socket_timeout_ms": "socket_timeout_ms",
        "tls": "tls",
        "topic": "topic",
        "type": "type",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineKafkaDestinationEncoding,
        id: str,
        inputs: List[str],
        topic: str,
        type: ObservabilityPipelineKafkaDestinationType,
        compression: Union[ObservabilityPipelineKafkaDestinationCompression, UnsetType] = unset,
        headers_key: Union[str, UnsetType] = unset,
        key_field: Union[str, UnsetType] = unset,
        librdkafka_options: Union[List[ObservabilityPipelineKafkaLibrdkafkaOption], UnsetType] = unset,
        message_timeout_ms: Union[int, UnsetType] = unset,
        rate_limit_duration_secs: Union[int, UnsetType] = unset,
        rate_limit_num: Union[int, UnsetType] = unset,
        sasl: Union[ObservabilityPipelineKafkaSasl, UnsetType] = unset,
        socket_timeout_ms: Union[int, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``kafka`` destination sends logs to Apache Kafka topics.

        **Supported pipeline types:** logs

        :param compression: Compression codec for Kafka messages.
        :type compression: ObservabilityPipelineKafkaDestinationCompression, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineKafkaDestinationEncoding

        :param headers_key: The field name to use for Kafka message headers.
        :type headers_key: str, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

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

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param topic: The Kafka topic name to publish logs to.
        :type topic: str

        :param type: The destination type. The value should always be ``kafka``.
        :type type: ObservabilityPipelineKafkaDestinationType
        """
        if compression is not unset:
            kwargs["compression"] = compression
        if headers_key is not unset:
            kwargs["headers_key"] = headers_key
        if key_field is not unset:
            kwargs["key_field"] = key_field
        if librdkafka_options is not unset:
            kwargs["librdkafka_options"] = librdkafka_options
        if message_timeout_ms is not unset:
            kwargs["message_timeout_ms"] = message_timeout_ms
        if rate_limit_duration_secs is not unset:
            kwargs["rate_limit_duration_secs"] = rate_limit_duration_secs
        if rate_limit_num is not unset:
            kwargs["rate_limit_num"] = rate_limit_num
        if sasl is not unset:
            kwargs["sasl"] = sasl
        if socket_timeout_ms is not unset:
            kwargs["socket_timeout_ms"] = socket_timeout_ms
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.id = id
        self_.inputs = inputs
        self_.topic = topic
        self_.type = type
