# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType(ModelSimple):
    """
    The minimal threshold type. The value should always be `always_keep`.

    :param value: If omitted defaults to "always_keep". Must be one of ["always_keep"].
    :type value: str
    """

    allowed_values = {
        "always_keep",
    }
    ALWAYS_KEEP: ClassVar["ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType.ALWAYS_KEEP = (
    ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType("always_keep")
)
