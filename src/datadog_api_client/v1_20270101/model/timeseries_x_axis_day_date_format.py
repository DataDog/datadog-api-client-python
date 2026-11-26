# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesXAxisDayDateFormat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["MMM d", "MMM d, yyyy", "MM/dd/yyyy", "dd/MM/yyyy", "MMMM d, yyyy", "auto"].
    :type value: str
    """

    allowed_values = {
        "MMM d",
        "MMM d, yyyy",
        "MM/dd/yyyy",
        "dd/MM/yyyy",
        "MMMM d, yyyy",
        "auto",
    }
    MMM_D: ClassVar["TimeseriesXAxisDayDateFormat"]
    MMM_D__YYYY: ClassVar["TimeseriesXAxisDayDateFormat"]
    MM_DD_YYYY: ClassVar["TimeseriesXAxisDayDateFormat"]
    DD_MM_YYYY: ClassVar["TimeseriesXAxisDayDateFormat"]
    MMMM_D__YYYY: ClassVar["TimeseriesXAxisDayDateFormat"]
    AUTO: ClassVar["TimeseriesXAxisDayDateFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesXAxisDayDateFormat.MMM_D = TimeseriesXAxisDayDateFormat("MMM d")
TimeseriesXAxisDayDateFormat.MMM_D__YYYY = TimeseriesXAxisDayDateFormat("MMM d, yyyy")
TimeseriesXAxisDayDateFormat.MM_DD_YYYY = TimeseriesXAxisDayDateFormat("MM/dd/yyyy")
TimeseriesXAxisDayDateFormat.DD_MM_YYYY = TimeseriesXAxisDayDateFormat("dd/MM/yyyy")
TimeseriesXAxisDayDateFormat.MMMM_D__YYYY = TimeseriesXAxisDayDateFormat("MMMM d, yyyy")
TimeseriesXAxisDayDateFormat.AUTO = TimeseriesXAxisDayDateFormat("auto")
