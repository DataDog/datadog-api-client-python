# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFunnelComputeAggregation(ModelSimple):
    """
    Aggregation type for user journey funnel compute.

    :param value: Must be one of ["cardinality", "count"].
    :type value: str
    """

    allowed_values = {
        "cardinality",
        "count",
    }
    CARDINALITY: ClassVar["ProductAnalyticsFunnelComputeAggregation"]
    COUNT: ClassVar["ProductAnalyticsFunnelComputeAggregation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFunnelComputeAggregation.CARDINALITY = ProductAnalyticsFunnelComputeAggregation("cardinality")
ProductAnalyticsFunnelComputeAggregation.COUNT = ProductAnalyticsFunnelComputeAggregation("count")
