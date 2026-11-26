# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DayOfTheMonth(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"].
    :type value: str
    """

    allowed_values = {
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    }
    ONE_ST: ClassVar["DayOfTheMonth"]
    TWO_ND: ClassVar["DayOfTheMonth"]
    THREE_RD: ClassVar["DayOfTheMonth"]
    FOUR_TH: ClassVar["DayOfTheMonth"]
    FIVE_TH: ClassVar["DayOfTheMonth"]
    SIX_TH: ClassVar["DayOfTheMonth"]
    SEVEN_TH: ClassVar["DayOfTheMonth"]
    EIGHT_TH: ClassVar["DayOfTheMonth"]
    NINE_TH: ClassVar["DayOfTheMonth"]
    TEN_TH: ClassVar["DayOfTheMonth"]
    ELEVEN_TH: ClassVar["DayOfTheMonth"]
    TWELVE_TH: ClassVar["DayOfTheMonth"]
    THIRTEEN_TH: ClassVar["DayOfTheMonth"]
    FOURTEEN_TH: ClassVar["DayOfTheMonth"]
    FIFTEEN_TH: ClassVar["DayOfTheMonth"]
    SIXTEEN_TH: ClassVar["DayOfTheMonth"]
    SEVENTEEN_TH: ClassVar["DayOfTheMonth"]
    EIGHTEEN_TH: ClassVar["DayOfTheMonth"]
    NINETEEN_TH: ClassVar["DayOfTheMonth"]
    TWENTY_TH: ClassVar["DayOfTheMonth"]
    TWENTY_ONE_ST: ClassVar["DayOfTheMonth"]
    TWENTY_TWO_ND: ClassVar["DayOfTheMonth"]
    TWENTY_THREE_RD: ClassVar["DayOfTheMonth"]
    TWENTY_FOUR_TH: ClassVar["DayOfTheMonth"]
    TWENTY_FIVE_TH: ClassVar["DayOfTheMonth"]
    TWENTY_SIX_TH: ClassVar["DayOfTheMonth"]
    TWENTY_SEVEN_TH: ClassVar["DayOfTheMonth"]
    TWENTY_EIGHT_TH: ClassVar["DayOfTheMonth"]
    TWENTY_NINE_TH: ClassVar["DayOfTheMonth"]
    THIRTY_TH: ClassVar["DayOfTheMonth"]
    THIRTY_ONE_ST: ClassVar["DayOfTheMonth"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DayOfTheMonth.ONE_ST = DayOfTheMonth("1st")
DayOfTheMonth.TWO_ND = DayOfTheMonth("2nd")
DayOfTheMonth.THREE_RD = DayOfTheMonth("3rd")
DayOfTheMonth.FOUR_TH = DayOfTheMonth("4th")
DayOfTheMonth.FIVE_TH = DayOfTheMonth("5th")
DayOfTheMonth.SIX_TH = DayOfTheMonth("6th")
DayOfTheMonth.SEVEN_TH = DayOfTheMonth("7th")
DayOfTheMonth.EIGHT_TH = DayOfTheMonth("8th")
DayOfTheMonth.NINE_TH = DayOfTheMonth("9th")
DayOfTheMonth.TEN_TH = DayOfTheMonth("10th")
DayOfTheMonth.ELEVEN_TH = DayOfTheMonth("11th")
DayOfTheMonth.TWELVE_TH = DayOfTheMonth("12th")
DayOfTheMonth.THIRTEEN_TH = DayOfTheMonth("13th")
DayOfTheMonth.FOURTEEN_TH = DayOfTheMonth("14th")
DayOfTheMonth.FIFTEEN_TH = DayOfTheMonth("15th")
DayOfTheMonth.SIXTEEN_TH = DayOfTheMonth("16th")
DayOfTheMonth.SEVENTEEN_TH = DayOfTheMonth("17th")
DayOfTheMonth.EIGHTEEN_TH = DayOfTheMonth("18th")
DayOfTheMonth.NINETEEN_TH = DayOfTheMonth("19th")
DayOfTheMonth.TWENTY_TH = DayOfTheMonth("20th")
DayOfTheMonth.TWENTY_ONE_ST = DayOfTheMonth("21st")
DayOfTheMonth.TWENTY_TWO_ND = DayOfTheMonth("22nd")
DayOfTheMonth.TWENTY_THREE_RD = DayOfTheMonth("23rd")
DayOfTheMonth.TWENTY_FOUR_TH = DayOfTheMonth("24th")
DayOfTheMonth.TWENTY_FIVE_TH = DayOfTheMonth("25th")
DayOfTheMonth.TWENTY_SIX_TH = DayOfTheMonth("26th")
DayOfTheMonth.TWENTY_SEVEN_TH = DayOfTheMonth("27th")
DayOfTheMonth.TWENTY_EIGHT_TH = DayOfTheMonth("28th")
DayOfTheMonth.TWENTY_NINE_TH = DayOfTheMonth("29th")
DayOfTheMonth.THIRTY_TH = DayOfTheMonth("30th")
DayOfTheMonth.THIRTY_ONE_ST = DayOfTheMonth("31st")
