# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PipelinePipelineKafkaSourceSaslMechanism(ModelSimple):
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
    PLAIN: ClassVar["PipelinePipelineKafkaSourceSaslMechanism"]
    SCRAMNOT_SHANOT_256: ClassVar["PipelinePipelineKafkaSourceSaslMechanism"]
    SCRAMNOT_SHANOT_512: ClassVar["PipelinePipelineKafkaSourceSaslMechanism"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PipelinePipelineKafkaSourceSaslMechanism.PLAIN = PipelinePipelineKafkaSourceSaslMechanism("PLAIN")
PipelinePipelineKafkaSourceSaslMechanism.SCRAMNOT_SHANOT_256 = PipelinePipelineKafkaSourceSaslMechanism("SCRAM-SHA-256")
PipelinePipelineKafkaSourceSaslMechanism.SCRAMNOT_SHANOT_512 = PipelinePipelineKafkaSourceSaslMechanism("SCRAM-SHA-512")
