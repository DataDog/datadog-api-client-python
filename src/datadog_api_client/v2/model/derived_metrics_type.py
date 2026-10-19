# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DerivedMetricsType(ModelSimple):
    """
    The derived metric resource type.

    :param value: If omitted defaults to "derived_metrics". Must be one of ["derived_metrics"].
    :type value: str
    """

    allowed_values = {
        "derived_metrics",
    }
    DERIVED_METRICS: ClassVar["DerivedMetricsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DerivedMetricsType.DERIVED_METRICS = DerivedMetricsType("derived_metrics")
