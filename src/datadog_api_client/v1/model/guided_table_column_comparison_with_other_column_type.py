# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableColumnComparisonWithOtherColumnType(ModelSimple):
    """


    :param value: Must be one of ["diff_from", "percent_of", "percent_diff_from"].
    :type value: str
    """

    allowed_values = {
        "diff_from",
        "percent_of",
        "percent_diff_from",
    }
    DIFF_FROM: ClassVar["GuidedTableColumnComparisonWithOtherColumnType"]
    PERCENT_OF: ClassVar["GuidedTableColumnComparisonWithOtherColumnType"]
    PERCENT_DIFF_FROM: ClassVar["GuidedTableColumnComparisonWithOtherColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableColumnComparisonWithOtherColumnType.DIFF_FROM = GuidedTableColumnComparisonWithOtherColumnType("diff_from")
GuidedTableColumnComparisonWithOtherColumnType.PERCENT_OF = GuidedTableColumnComparisonWithOtherColumnType("percent_of")
GuidedTableColumnComparisonWithOtherColumnType.PERCENT_DIFF_FROM = GuidedTableColumnComparisonWithOtherColumnType(
    "percent_diff_from"
)
