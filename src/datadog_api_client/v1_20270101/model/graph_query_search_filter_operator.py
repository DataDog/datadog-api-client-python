# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GraphQuerySearchFilterOperator(ModelSimple):
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
    EQ: ClassVar["GraphQuerySearchFilterOperator"]
    GT: ClassVar["GraphQuerySearchFilterOperator"]
    GT_EQ: ClassVar["GraphQuerySearchFilterOperator"]
    LT: ClassVar["GraphQuerySearchFilterOperator"]
    LT_EQ: ClassVar["GraphQuerySearchFilterOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GraphQuerySearchFilterOperator.EQ = GraphQuerySearchFilterOperator("=")
GraphQuerySearchFilterOperator.GT = GraphQuerySearchFilterOperator(">")
GraphQuerySearchFilterOperator.GT_EQ = GraphQuerySearchFilterOperator(">=")
GraphQuerySearchFilterOperator.LT = GraphQuerySearchFilterOperator("<")
GraphQuerySearchFilterOperator.LT_EQ = GraphQuerySearchFilterOperator("<=")
