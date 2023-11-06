# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class TimeseriesFormulaResponseType(StringEnum):
    """
    The type of the resource. The value should always be timeseries_response.

    :param value: If omitted defaults to "timeseries_response". Must be one of ["timeseries_response"].
    :type value: str
    """

    allowed_values = {
        "timeseries_response",
    }
    TIMESERIES_RESPONSE: ClassVar["TimeseriesFormulaResponseType"]


TimeseriesFormulaResponseType.TIMESERIES_RESPONSE = TimeseriesFormulaResponseType("timeseries_response")
