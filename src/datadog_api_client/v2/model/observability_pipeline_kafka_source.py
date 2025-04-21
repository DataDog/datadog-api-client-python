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
    from datadog_api_client.v2.model.observability_pipeline_kafka_source_librdkafka_option import (
        ObservabilityPipelineKafkaSourceLibrdkafkaOption,
    )
    from datadog_api_client.v2.model.observability_pipeline_kafka_source_sasl import (
        ObservabilityPipelineKafkaSourceSasl,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_kafka_source_type import (
        ObservabilityPipelineKafkaSourceType,
    )


class ObservabilityPipelineKafkaSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_kafka_source_librdkafka_option import (
            ObservabilityPipelineKafkaSourceLibrdkafkaOption,
        )
        from datadog_api_client.v2.model.observability_pipeline_kafka_source_sasl import (
            ObservabilityPipelineKafkaSourceSasl,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_kafka_source_type import (
            ObservabilityPipelineKafkaSourceType,
        )

        return {
            "group_id": (str,),
            "id": (str,),
            "librdkafka_options": ([ObservabilityPipelineKafkaSourceLibrdkafkaOption],),
            "sasl": (ObservabilityPipelineKafkaSourceSasl,),
            "tls": (ObservabilityPipelineTls,),
            "topics": ([str],),
            "type": (ObservabilityPipelineKafkaSourceType,),
        }

    attribute_map = {
        "group_id": "group_id",
        "id": "id",
        "librdkafka_options": "librdkafka_options",
        "sasl": "sasl",
        "tls": "tls",
        "topics": "topics",
        "type": "type",
    }

    def __init__(
        self_,
        group_id: str,
        id: str,
        topics: List[str],
        type: ObservabilityPipelineKafkaSourceType,
        librdkafka_options: Union[List[ObservabilityPipelineKafkaSourceLibrdkafkaOption], UnsetType] = unset,
        sasl: Union[ObservabilityPipelineKafkaSourceSasl, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``kafka`` source ingests data from Apache Kafka topics.

        :param group_id: Consumer group ID used by the Kafka client.
        :type group_id: str

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param librdkafka_options: Optional list of advanced Kafka client configuration options, defined as key-value pairs.
        :type librdkafka_options: [ObservabilityPipelineKafkaSourceLibrdkafkaOption], optional

        :param sasl: Specifies the SASL mechanism for authenticating with a Kafka cluster.
        :type sasl: ObservabilityPipelineKafkaSourceSasl, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param topics: A list of Kafka topic names to subscribe to. The source ingests messages from each topic specified.
        :type topics: [str]

        :param type: The source type. The value should always be ``kafka``.
        :type type: ObservabilityPipelineKafkaSourceType
        """
        if librdkafka_options is not unset:
            kwargs["librdkafka_options"] = librdkafka_options
        if sasl is not unset:
            kwargs["sasl"] = sasl
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.group_id = group_id
        self_.id = id
        self_.topics = topics
        self_.type = type
