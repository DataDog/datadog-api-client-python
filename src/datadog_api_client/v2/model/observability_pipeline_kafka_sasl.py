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
    from datadog_api_client.v2.model.observability_pipeline_kafka_sasl_mechanism import (
        ObservabilityPipelineKafkaSaslMechanism,
    )


class ObservabilityPipelineKafkaSasl(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_kafka_sasl_mechanism import (
            ObservabilityPipelineKafkaSaslMechanism,
        )

        return {
            "mechanism": (ObservabilityPipelineKafkaSaslMechanism,),
            "password_key": (str,),
            "username_key": (str,),
        }

    attribute_map = {
        "mechanism": "mechanism",
        "password_key": "password_key",
        "username_key": "username_key",
    }

    def __init__(
        self_,
        mechanism: Union[ObservabilityPipelineKafkaSaslMechanism, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Specifies the SASL mechanism for authenticating with a Kafka cluster.

        :param mechanism: SASL mechanism used for Kafka authentication.
        :type mechanism: ObservabilityPipelineKafkaSaslMechanism, optional

        :param password_key: Name of the environment variable or secret that holds the SASL password.
        :type password_key: str, optional

        :param username_key: Name of the environment variable or secret that holds the SASL username.
        :type username_key: str, optional
        """
        if mechanism is not unset:
            kwargs["mechanism"] = mechanism
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if username_key is not unset:
            kwargs["username_key"] = username_key
        super().__init__(kwargs)
