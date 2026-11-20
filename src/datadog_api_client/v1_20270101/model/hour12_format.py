# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Hour12Format(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["12am", "1am", "2am", "3am", "4am", "5am", "6am", "7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm", "11pm"].
    :type value: str
    """

    allowed_values = {
        "12am",
        "1am",
        "2am",
        "3am",
        "4am",
        "5am",
        "6am",
        "7am",
        "8am",
        "9am",
        "10am",
        "11am",
        "12pm",
        "1pm",
        "2pm",
        "3pm",
        "4pm",
        "5pm",
        "6pm",
        "7pm",
        "8pm",
        "9pm",
        "10pm",
        "11pm",
    }
    TWELVE_AM: ClassVar["Hour12Format"]
    ONE_AM: ClassVar["Hour12Format"]
    TWO_AM: ClassVar["Hour12Format"]
    THREE_AM: ClassVar["Hour12Format"]
    FOUR_AM: ClassVar["Hour12Format"]
    FIVE_AM: ClassVar["Hour12Format"]
    SIX_AM: ClassVar["Hour12Format"]
    SEVEN_AM: ClassVar["Hour12Format"]
    EIGHT_AM: ClassVar["Hour12Format"]
    NINE_AM: ClassVar["Hour12Format"]
    TEN_AM: ClassVar["Hour12Format"]
    ELEVEN_AM: ClassVar["Hour12Format"]
    TWELVE_PM: ClassVar["Hour12Format"]
    ONE_PM: ClassVar["Hour12Format"]
    TWO_PM: ClassVar["Hour12Format"]
    THREE_PM: ClassVar["Hour12Format"]
    FOUR_PM: ClassVar["Hour12Format"]
    FIVE_PM: ClassVar["Hour12Format"]
    SIX_PM: ClassVar["Hour12Format"]
    SEVEN_PM: ClassVar["Hour12Format"]
    EIGHT_PM: ClassVar["Hour12Format"]
    NINE_PM: ClassVar["Hour12Format"]
    TEN_PM: ClassVar["Hour12Format"]
    ELEVEN_PM: ClassVar["Hour12Format"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Hour12Format.TWELVE_AM = Hour12Format("12am")
Hour12Format.ONE_AM = Hour12Format("1am")
Hour12Format.TWO_AM = Hour12Format("2am")
Hour12Format.THREE_AM = Hour12Format("3am")
Hour12Format.FOUR_AM = Hour12Format("4am")
Hour12Format.FIVE_AM = Hour12Format("5am")
Hour12Format.SIX_AM = Hour12Format("6am")
Hour12Format.SEVEN_AM = Hour12Format("7am")
Hour12Format.EIGHT_AM = Hour12Format("8am")
Hour12Format.NINE_AM = Hour12Format("9am")
Hour12Format.TEN_AM = Hour12Format("10am")
Hour12Format.ELEVEN_AM = Hour12Format("11am")
Hour12Format.TWELVE_PM = Hour12Format("12pm")
Hour12Format.ONE_PM = Hour12Format("1pm")
Hour12Format.TWO_PM = Hour12Format("2pm")
Hour12Format.THREE_PM = Hour12Format("3pm")
Hour12Format.FOUR_PM = Hour12Format("4pm")
Hour12Format.FIVE_PM = Hour12Format("5pm")
Hour12Format.SIX_PM = Hour12Format("6pm")
Hour12Format.SEVEN_PM = Hour12Format("7pm")
Hour12Format.EIGHT_PM = Hour12Format("8pm")
Hour12Format.NINE_PM = Hour12Format("9pm")
Hour12Format.TEN_PM = Hour12Format("10pm")
Hour12Format.ELEVEN_PM = Hour12Format("11pm")
