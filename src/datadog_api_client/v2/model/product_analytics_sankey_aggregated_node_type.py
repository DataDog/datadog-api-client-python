# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsSankeyAggregatedNodeType(ModelSimple):
    """


    :param value: If omitted defaults to "aggregated". Must be one of ["aggregated"].
    :type value: str
    """

    allowed_values = {
        "aggregated",
    }
    AGGREGATED: ClassVar["ProductAnalyticsSankeyAggregatedNodeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsSankeyAggregatedNodeType.AGGREGATED = ProductAnalyticsSankeyAggregatedNodeType("aggregated")
