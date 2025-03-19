# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StateVariableType(ModelSimple):
    """
    The state variable type.

    :param value: If omitted defaults to "stateVariable". Must be one of ["stateVariable"].
    :type value: str
    """

    allowed_values = {
        "stateVariable",
    }
    STATEVARIABLE: ClassVar["StateVariableType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StateVariableType.STATEVARIABLE = StateVariableType("stateVariable")
