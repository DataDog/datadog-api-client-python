# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HeatgridTextFormatMatchType(ModelSimple):
    """
    Comparison used to match a group label.

    :param value: Must be one of ["is", "is_not", "contains", "does_not_contain", "starts_with", "ends_with"].
    :type value: str
    """

    allowed_values = {
        "is",
        "is_not",
        "contains",
        "does_not_contain",
        "starts_with",
        "ends_with",
    }
    IS: ClassVar["HeatgridTextFormatMatchType"]
    IS_NOT: ClassVar["HeatgridTextFormatMatchType"]
    CONTAINS: ClassVar["HeatgridTextFormatMatchType"]
    DOES_NOT_CONTAIN: ClassVar["HeatgridTextFormatMatchType"]
    STARTS_WITH: ClassVar["HeatgridTextFormatMatchType"]
    ENDS_WITH: ClassVar["HeatgridTextFormatMatchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HeatgridTextFormatMatchType.IS = HeatgridTextFormatMatchType("is")
HeatgridTextFormatMatchType.IS_NOT = HeatgridTextFormatMatchType("is_not")
HeatgridTextFormatMatchType.CONTAINS = HeatgridTextFormatMatchType("contains")
HeatgridTextFormatMatchType.DOES_NOT_CONTAIN = HeatgridTextFormatMatchType("does_not_contain")
HeatgridTextFormatMatchType.STARTS_WITH = HeatgridTextFormatMatchType("starts_with")
HeatgridTextFormatMatchType.ENDS_WITH = HeatgridTextFormatMatchType("ends_with")
