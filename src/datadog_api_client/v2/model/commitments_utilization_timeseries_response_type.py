# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsUtilizationTimeseriesResponseType(ModelSimple):
    """
    Type of the timeseries utilization response resource.

    :param value: If omitted defaults to "utilization_timeseries_response". Must be one of ["utilization_timeseries_response"].
    :type value: str
    """

    allowed_values = {
        "utilization_timeseries_response",
    }
    UTILIZATION_TIMESERIES_RESPONSE: ClassVar["CommitmentsUtilizationTimeseriesResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsUtilizationTimeseriesResponseType.UTILIZATION_TIMESERIES_RESPONSE = (
    CommitmentsUtilizationTimeseriesResponseType("utilization_timeseries_response")
)
