# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionResponseFormat(ModelSimple):
    """
    Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets.

    :param value: Must be one of ["timeseries", "scalar", "event_list"].
    :type value: str
    """

    allowed_values = {
        "timeseries",
        "scalar",
        "event_list",
    }
    TIMESERIES: ClassVar["FormulaAndFunctionResponseFormat"]
    SCALAR: ClassVar["FormulaAndFunctionResponseFormat"]
    EVENT_LIST: ClassVar["FormulaAndFunctionResponseFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionResponseFormat.TIMESERIES = FormulaAndFunctionResponseFormat("timeseries")
FormulaAndFunctionResponseFormat.SCALAR = FormulaAndFunctionResponseFormat("scalar")
FormulaAndFunctionResponseFormat.EVENT_LIST = FormulaAndFunctionResponseFormat("event_list")
