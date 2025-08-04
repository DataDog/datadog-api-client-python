# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketDestinationType(ModelSimple):
    """
    The destination type. The value should always be `socket`.

    :param value: If omitted defaults to "socket". Must be one of ["socket"].
    :type value: str
    """

    allowed_values = {
        "socket",
    }
    SOCKET: ClassVar["ObservabilityPipelineSocketDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketDestinationType.SOCKET = ObservabilityPipelineSocketDestinationType("socket")
