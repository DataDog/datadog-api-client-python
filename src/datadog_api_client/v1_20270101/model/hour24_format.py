# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Hour24Format(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"].
    :type value: str
    """

    allowed_values = {
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
    }
    ZERO: ClassVar["Hour24Format"]
    ONE: ClassVar["Hour24Format"]
    TWO: ClassVar["Hour24Format"]
    THREE: ClassVar["Hour24Format"]
    FOUR: ClassVar["Hour24Format"]
    FIVE: ClassVar["Hour24Format"]
    SIX: ClassVar["Hour24Format"]
    SEVEN: ClassVar["Hour24Format"]
    EIGHT: ClassVar["Hour24Format"]
    NINE: ClassVar["Hour24Format"]
    TEN: ClassVar["Hour24Format"]
    ELEVEN: ClassVar["Hour24Format"]
    TWELVE: ClassVar["Hour24Format"]
    THIRTEEN: ClassVar["Hour24Format"]
    FOURTEEN: ClassVar["Hour24Format"]
    FIFTEEN: ClassVar["Hour24Format"]
    SIXTEEN: ClassVar["Hour24Format"]
    SEVENTEEN: ClassVar["Hour24Format"]
    EIGHTEEN: ClassVar["Hour24Format"]
    NINETEEN: ClassVar["Hour24Format"]
    TWENTY: ClassVar["Hour24Format"]
    TWENTY_ONE: ClassVar["Hour24Format"]
    TWENTY_TWO: ClassVar["Hour24Format"]
    TWENTY_THREE: ClassVar["Hour24Format"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Hour24Format.ZERO = Hour24Format("0")
Hour24Format.ONE = Hour24Format("1")
Hour24Format.TWO = Hour24Format("2")
Hour24Format.THREE = Hour24Format("3")
Hour24Format.FOUR = Hour24Format("4")
Hour24Format.FIVE = Hour24Format("5")
Hour24Format.SIX = Hour24Format("6")
Hour24Format.SEVEN = Hour24Format("7")
Hour24Format.EIGHT = Hour24Format("8")
Hour24Format.NINE = Hour24Format("9")
Hour24Format.TEN = Hour24Format("10")
Hour24Format.ELEVEN = Hour24Format("11")
Hour24Format.TWELVE = Hour24Format("12")
Hour24Format.THIRTEEN = Hour24Format("13")
Hour24Format.FOURTEEN = Hour24Format("14")
Hour24Format.FIFTEEN = Hour24Format("15")
Hour24Format.SIXTEEN = Hour24Format("16")
Hour24Format.SEVENTEEN = Hour24Format("17")
Hour24Format.EIGHTEEN = Hour24Format("18")
Hour24Format.NINETEEN = Hour24Format("19")
Hour24Format.TWENTY = Hour24Format("20")
Hour24Format.TWENTY_ONE = Hour24Format("21")
Hour24Format.TWENTY_TWO = Hour24Format("22")
Hour24Format.TWENTY_THREE = Hour24Format("23")
