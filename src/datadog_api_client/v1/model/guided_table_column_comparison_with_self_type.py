# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableColumnComparisonWithSelfType(ModelSimple):
    """


    :param value: If omitted defaults to "percent_column_total". Must be one of ["percent_column_total"].
    :type value: str
    """

    allowed_values = {
        "percent_column_total",
    }
    PERCENT_COLUMN_TOTAL: ClassVar["GuidedTableColumnComparisonWithSelfType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableColumnComparisonWithSelfType.PERCENT_COLUMN_TOTAL = GuidedTableColumnComparisonWithSelfType(
    "percent_column_total"
)
