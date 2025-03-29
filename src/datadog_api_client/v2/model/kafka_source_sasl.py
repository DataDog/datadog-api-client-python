# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.kafka_source_sasl_mechanism import KafkaSourceSaslMechanism


class KafkaSourceSasl(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.kafka_source_sasl_mechanism import KafkaSourceSaslMechanism

        return {
            "mechanism": (KafkaSourceSaslMechanism,),
        }

    attribute_map = {
        "mechanism": "mechanism",
    }

    def __init__(self_, mechanism: Union[KafkaSourceSaslMechanism, UnsetType] = unset, **kwargs):
        """
        The definition of ``KafkaSourceSasl`` object.

        :param mechanism: The definition of ``KafkaSourceSaslMechanism`` object.
        :type mechanism: KafkaSourceSaslMechanism, optional
        """
        if mechanism is not unset:
            kwargs["mechanism"] = mechanism
        super().__init__(kwargs)
