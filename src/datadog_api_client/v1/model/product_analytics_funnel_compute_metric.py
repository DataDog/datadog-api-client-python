# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFunnelComputeMetric(ModelSimple):
    """
    Metric for user journey funnel compute. `__dd.conversion` and `__dd.conversion_rate` accept `count` (unique users/sessions) and `cardinality` (total users/sessions) as aggregations.

    :param value: Must be one of ["__dd.conversion", "__dd.conversion_rate"].
    :type value: str
    """

    allowed_values = {
        "__dd.conversion",
        "__dd.conversion_rate",
    }
    CONVERSION: ClassVar["ProductAnalyticsFunnelComputeMetric"]
    CONVERSION_RATE: ClassVar["ProductAnalyticsFunnelComputeMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFunnelComputeMetric.CONVERSION = ProductAnalyticsFunnelComputeMetric("__dd.conversion")
ProductAnalyticsFunnelComputeMetric.CONVERSION_RATE = ProductAnalyticsFunnelComputeMetric("__dd.conversion_rate")
