# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Month(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"].
    :type value: str
    """

    allowed_values = {
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    }
    JANUARY: ClassVar["Month"]
    FEBRUARY: ClassVar["Month"]
    MARCH: ClassVar["Month"]
    APRIL: ClassVar["Month"]
    MAY: ClassVar["Month"]
    JUNE: ClassVar["Month"]
    JULY: ClassVar["Month"]
    AUGUST: ClassVar["Month"]
    SEPTEMBER: ClassVar["Month"]
    OCTOBER: ClassVar["Month"]
    NOVEMBER: ClassVar["Month"]
    DECEMBER: ClassVar["Month"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Month.JANUARY = Month("january")
Month.FEBRUARY = Month("february")
Month.MARCH = Month("march")
Month.APRIL = Month("april")
Month.MAY = Month("may")
Month.JUNE = Month("june")
Month.JULY = Month("july")
Month.AUGUST = Month("august")
Month.SEPTEMBER = Month("september")
Month.OCTOBER = Month("october")
Month.NOVEMBER = Month("november")
Month.DECEMBER = Month("december")
