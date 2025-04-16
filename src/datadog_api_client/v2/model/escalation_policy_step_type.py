# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EscalationPolicyStepType(ModelSimple):
    """
    Indicates that the resource is of type `steps`.

    :param value: If omitted defaults to "steps". Must be one of ["steps"].
    :type value: str
    """

    allowed_values = {
        "steps",
    }
    STEPS: ClassVar["EscalationPolicyStepType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EscalationPolicyStepType.STEPS = EscalationPolicyStepType("steps")
