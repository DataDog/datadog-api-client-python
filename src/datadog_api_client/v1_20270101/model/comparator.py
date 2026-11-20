# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Comparator(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["=", ">", ">=", "<", "<="].
    :type value: str
    """

    allowed_values = {
        "=",
        ">",
        ">=",
        "<",
        "<=",
    }
    EQ: ClassVar["Comparator"]
    GT: ClassVar["Comparator"]
    GT_EQ: ClassVar["Comparator"]
    LT: ClassVar["Comparator"]
    LT_EQ: ClassVar["Comparator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Comparator.EQ = Comparator("=")
Comparator.GT = Comparator(">")
Comparator.GT_EQ = Comparator(">=")
Comparator.LT = Comparator("<")
Comparator.LT_EQ = Comparator("<=")
