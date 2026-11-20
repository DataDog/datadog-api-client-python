# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesXAxisMonthDateFormat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["auto", "MMM", "MMM yyyy", "MM/yyyy", "MMMM yyyy"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "MMM",
        "MMM yyyy",
        "MM/yyyy",
        "MMMM yyyy",
    }
    AUTO: ClassVar["TimeseriesXAxisMonthDateFormat"]
    MMM: ClassVar["TimeseriesXAxisMonthDateFormat"]
    MMM_YYYY: ClassVar["TimeseriesXAxisMonthDateFormat"]
    MM_YYYY: ClassVar["TimeseriesXAxisMonthDateFormat"]
    MMMM_YYYY: ClassVar["TimeseriesXAxisMonthDateFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesXAxisMonthDateFormat.AUTO = TimeseriesXAxisMonthDateFormat("auto")
TimeseriesXAxisMonthDateFormat.MMM = TimeseriesXAxisMonthDateFormat("MMM")
TimeseriesXAxisMonthDateFormat.MMM_YYYY = TimeseriesXAxisMonthDateFormat("MMM yyyy")
TimeseriesXAxisMonthDateFormat.MM_YYYY = TimeseriesXAxisMonthDateFormat("MM/yyyy")
TimeseriesXAxisMonthDateFormat.MMMM_YYYY = TimeseriesXAxisMonthDateFormat("MMMM yyyy")
