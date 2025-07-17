# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketDestinationMode(ModelSimple):
    """
    Protocol used to send logs.

    :param value: Must be one of ["tcp", "udp"].
    :type value: str
    """

    allowed_values = {
        "tcp",
        "udp",
    }
    TCP: ClassVar["ObservabilityPipelineSocketDestinationMode"]
    UDP: ClassVar["ObservabilityPipelineSocketDestinationMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketDestinationMode.TCP = ObservabilityPipelineSocketDestinationMode("tcp")
ObservabilityPipelineSocketDestinationMode.UDP = ObservabilityPipelineSocketDestinationMode("udp")
