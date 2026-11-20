# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TreeDataProjectionBarChartType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "bar_chart". Must be one of ["bar_chart"].
    :type value: str
    """

    allowed_values = {
        "bar_chart",
    }
    BAR_CHART: ClassVar["TreeDataProjectionBarChartType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TreeDataProjectionBarChartType.BAR_CHART = TreeDataProjectionBarChartType("bar_chart")
