# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumMetricType(ModelSimple):
    """
    The type of the resource. The value should always be rum_metrics.

    :param value: If omitted defaults to "rum_metrics". Must be one of ["rum_metrics"].
    :type value: str
    """

    allowed_values = {
        "rum_metrics",
    }
    RUM_METRICS: ClassVar["RumMetricType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumMetricType.RUM_METRICS = RumMetricType("rum_metrics")
