# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostTagMetadataDailyFilter(ModelSimple):
    """
    Granularity for tag metadata results. `true` returns one row per day, `false` (or omitted) returns the monthly roll-up.

    :param value: Must be one of ["true", "false"].
    :type value: str
    """

    allowed_values = {
        "true",
        "false",
    }
    TRUE: ClassVar["CostTagMetadataDailyFilter"]
    FALSE: ClassVar["CostTagMetadataDailyFilter"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostTagMetadataDailyFilter.TRUE = CostTagMetadataDailyFilter("true")
CostTagMetadataDailyFilter.FALSE = CostTagMetadataDailyFilter("false")
