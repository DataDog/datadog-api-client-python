# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsSavingsTimeseriesResponseType(ModelSimple):
    """
    Type of the timeseries savings response resource.

    :param value: If omitted defaults to "savings_timeseries_response". Must be one of ["savings_timeseries_response"].
    :type value: str
    """

    allowed_values = {
        "savings_timeseries_response",
    }
    SAVINGS_TIMESERIES_RESPONSE: ClassVar["CommitmentsSavingsTimeseriesResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsSavingsTimeseriesResponseType.SAVINGS_TIMESERIES_RESPONSE = CommitmentsSavingsTimeseriesResponseType(
    "savings_timeseries_response"
)
