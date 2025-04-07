# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelinePipelineKafkaSourceSaslMechanism(ModelSimple):
    """
    SASL mechanism used for Kafka authentication.

    :param value: Must be one of ["PLAIN", "SCRAM-SHA-256", "SCRAM-SHA-512"].
    :type value: str
    """

    allowed_values = {
        "PLAIN",
        "SCRAM-SHA-256",
        "SCRAM-SHA-512",
    }
    PLAIN: ClassVar["ObservabilityPipelinePipelineKafkaSourceSaslMechanism"]
    SCRAMNOT_SHANOT_256: ClassVar["ObservabilityPipelinePipelineKafkaSourceSaslMechanism"]
    SCRAMNOT_SHANOT_512: ClassVar["ObservabilityPipelinePipelineKafkaSourceSaslMechanism"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelinePipelineKafkaSourceSaslMechanism.PLAIN = ObservabilityPipelinePipelineKafkaSourceSaslMechanism(
    "PLAIN"
)
ObservabilityPipelinePipelineKafkaSourceSaslMechanism.SCRAMNOT_SHANOT_256 = (
    ObservabilityPipelinePipelineKafkaSourceSaslMechanism("SCRAM-SHA-256")
)
ObservabilityPipelinePipelineKafkaSourceSaslMechanism.SCRAMNOT_SHANOT_512 = (
    ObservabilityPipelinePipelineKafkaSourceSaslMechanism("SCRAM-SHA-512")
)
