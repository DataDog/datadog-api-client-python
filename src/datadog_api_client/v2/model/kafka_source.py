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
    from datadog_api_client.v2.model.kafka_source_librdkafka_options_items import KafkaSourceLibrdkafkaOptionsItems
    from datadog_api_client.v2.model.kafka_source_sasl import KafkaSourceSasl
    from datadog_api_client.v2.model.tls import Tls
    from datadog_api_client.v2.model.kafka_source_type import KafkaSourceType


class KafkaSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.kafka_source_librdkafka_options_items import KafkaSourceLibrdkafkaOptionsItems
        from datadog_api_client.v2.model.kafka_source_sasl import KafkaSourceSasl
        from datadog_api_client.v2.model.tls import Tls
        from datadog_api_client.v2.model.kafka_source_type import KafkaSourceType

        return {
            "group_id": (str,),
            "id": (str,),
            "librdkafka_options": ([KafkaSourceLibrdkafkaOptionsItems],),
            "sasl": (KafkaSourceSasl,),
            "tls": (Tls,),
            "topics": ([str],),
            "type": (KafkaSourceType,),
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
        type: KafkaSourceType,
        librdkafka_options: Union[List[KafkaSourceLibrdkafkaOptionsItems], UnsetType] = unset,
        sasl: Union[KafkaSourceSasl, UnsetType] = unset,
        tls: Union[Tls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``kafka`` source ingests data from Apache Kafka topics.

        :param group_id: The ``KafkaSource`` ``group_id``.
        :type group_id: str

        :param id: The ``KafkaSource`` ``id``.
        :type id: str

        :param librdkafka_options: The ``KafkaSource`` ``librdkafka_options``.
        :type librdkafka_options: [KafkaSourceLibrdkafkaOptionsItems], optional

        :param sasl: The definition of ``KafkaSourceSasl`` object.
        :type sasl: KafkaSourceSasl, optional

        :param tls: The definition of ``Tls`` object.
        :type tls: Tls, optional

        :param topics: The ``KafkaSource`` ``topics``.
        :type topics: [str]

        :param type: The definition of ``KafkaSourceType`` object.
        :type type: KafkaSourceType
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
