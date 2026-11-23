# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsCoverageTimeseriesResponseType(ModelSimple):
    """
    Type of the timeseries coverage response resource.

    :param value: If omitted defaults to "coverage_timeseries_response". Must be one of ["coverage_timeseries_response"].
    :type value: str
    """

    allowed_values = {
        "coverage_timeseries_response",
    }
    COVERAGE_TIMESERIES_RESPONSE: ClassVar["CommitmentsCoverageTimeseriesResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsCoverageTimeseriesResponseType.COVERAGE_TIMESERIES_RESPONSE = CommitmentsCoverageTimeseriesResponseType(
    "coverage_timeseries_response"
)
