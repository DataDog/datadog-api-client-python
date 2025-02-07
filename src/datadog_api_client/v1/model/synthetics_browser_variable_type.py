# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBrowserVariableType(ModelSimple):
    """
    Type of browser test variable.

    :param value: Must be one of ["element", "email", "global", "text"].
    :type value: str
    """

    allowed_values = {
        "element",
        "email",
        "global",
        "text",
    }
    ELEMENT: ClassVar["SyntheticsBrowserVariableType"]
    EMAIL: ClassVar["SyntheticsBrowserVariableType"]
    GLOBAL: ClassVar["SyntheticsBrowserVariableType"]
    TEXT: ClassVar["SyntheticsBrowserVariableType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBrowserVariableType.ELEMENT = SyntheticsBrowserVariableType("element")
SyntheticsBrowserVariableType.EMAIL = SyntheticsBrowserVariableType("email")
SyntheticsBrowserVariableType.GLOBAL = SyntheticsBrowserVariableType("global")
SyntheticsBrowserVariableType.TEXT = SyntheticsBrowserVariableType("text")
