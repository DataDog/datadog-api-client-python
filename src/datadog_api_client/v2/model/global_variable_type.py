# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GlobalVariableType(ModelSimple):
    """
    Global variable type.

    :param value: If omitted defaults to "global_variables". Must be one of ["global_variables"].
    :type value: str
    """

    allowed_values = {
        "global_variables",
    }
    GLOBAL_VARIABLES: ClassVar["GlobalVariableType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GlobalVariableType.GLOBAL_VARIABLES = GlobalVariableType("global_variables")
