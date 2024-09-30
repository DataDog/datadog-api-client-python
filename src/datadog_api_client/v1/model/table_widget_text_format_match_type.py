# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TableWidgetTextFormatMatchType(ModelSimple):
    """
    Match or compare option.

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
    IS: ClassVar["TableWidgetTextFormatMatchType"]
    IS_NOT: ClassVar["TableWidgetTextFormatMatchType"]
    CONTAINS: ClassVar["TableWidgetTextFormatMatchType"]
    DOES_NOT_CONTAIN: ClassVar["TableWidgetTextFormatMatchType"]
    STARTS_WITH: ClassVar["TableWidgetTextFormatMatchType"]
    ENDS_WITH: ClassVar["TableWidgetTextFormatMatchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TableWidgetTextFormatMatchType.IS = TableWidgetTextFormatMatchType("is")
TableWidgetTextFormatMatchType.IS_NOT = TableWidgetTextFormatMatchType("is_not")
TableWidgetTextFormatMatchType.CONTAINS = TableWidgetTextFormatMatchType("contains")
TableWidgetTextFormatMatchType.DOES_NOT_CONTAIN = TableWidgetTextFormatMatchType("does_not_contain")
TableWidgetTextFormatMatchType.STARTS_WITH = TableWidgetTextFormatMatchType("starts_with")
TableWidgetTextFormatMatchType.ENDS_WITH = TableWidgetTextFormatMatchType("ends_with")
