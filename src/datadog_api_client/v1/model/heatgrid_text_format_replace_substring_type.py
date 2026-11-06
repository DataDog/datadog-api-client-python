# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HeatgridTextFormatReplaceSubstringType(ModelSimple):
    """
    Replace a substring of a matching group label.

    :param value: If omitted defaults to "substring". Must be one of ["substring"].
    :type value: str
    """

    allowed_values = {
        "substring",
    }
    SUBSTRING: ClassVar["HeatgridTextFormatReplaceSubstringType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HeatgridTextFormatReplaceSubstringType.SUBSTRING = HeatgridTextFormatReplaceSubstringType("substring")
