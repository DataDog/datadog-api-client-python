# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostAggregationType(ModelSimple):
    """
    Controls how costs are aggregated when using `start_date`. The `cumulative` option returns month-to-date running totals.

    :param value: If omitted defaults to "cumulative". Must be one of ["cumulative"].
    :type value: str
    """

    allowed_values = {
        "cumulative",
    }
    CUMULATIVE: ClassVar["CostAggregationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostAggregationType.CUMULATIVE = CostAggregationType("cumulative")
