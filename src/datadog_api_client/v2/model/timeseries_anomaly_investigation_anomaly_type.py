# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationAnomalyType(ModelSimple):
    """
    Direction of an anomaly relative to its expected range.

    :param value: Must be one of ["spike", "dip"].
    :type value: str
    """

    allowed_values = {
        "spike",
        "dip",
    }
    SPIKE: ClassVar["TimeseriesAnomalyInvestigationAnomalyType"]
    DIP: ClassVar["TimeseriesAnomalyInvestigationAnomalyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationAnomalyType.SPIKE = TimeseriesAnomalyInvestigationAnomalyType("spike")
TimeseriesAnomalyInvestigationAnomalyType.DIP = TimeseriesAnomalyInvestigationAnomalyType("dip")
