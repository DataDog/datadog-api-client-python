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
    from datadog_api_client.v2.model.observability_pipeline_pipeline_kafka_source_sasl_mechanism import (
        ObservabilityPipelinePipelineKafkaSourceSaslMechanism,
    )


class ObservabilityPipelineKafkaSourceSasl(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_pipeline_kafka_source_sasl_mechanism import (
            ObservabilityPipelinePipelineKafkaSourceSaslMechanism,
        )

        return {
            "mechanism": (ObservabilityPipelinePipelineKafkaSourceSaslMechanism,),
        }

    attribute_map = {
        "mechanism": "mechanism",
    }

    def __init__(
        self_, mechanism: Union[ObservabilityPipelinePipelineKafkaSourceSaslMechanism, UnsetType] = unset, **kwargs
    ):
        """
        Specifies the SASL mechanism for authenticating with a Kafka cluster.

        :param mechanism: SASL mechanism used for Kafka authentication.
        :type mechanism: ObservabilityPipelinePipelineKafkaSourceSaslMechanism, optional
        """
        if mechanism is not unset:
            kwargs["mechanism"] = mechanism
        super().__init__(kwargs)
