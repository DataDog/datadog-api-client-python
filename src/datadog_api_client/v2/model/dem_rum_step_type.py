# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DemRumStepType(ModelSimple):
    """
    The type of a RUM journey step.

    :param value: Must be one of ["start", "stop", "step"].
    :type value: str
    """

    allowed_values = {
        "start",
        "stop",
        "step",
    }
    START: ClassVar["DemRumStepType"]
    STOP: ClassVar["DemRumStepType"]
    STEP: ClassVar["DemRumStepType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DemRumStepType.START = DemRumStepType("start")
DemRumStepType.STOP = DemRumStepType("stop")
DemRumStepType.STEP = DemRumStepType("step")
