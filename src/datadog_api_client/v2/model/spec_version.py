# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SpecVersion(ModelSimple):
    """
    The version of the CycloneDX specification a BOM conforms to.

    :param value: Must be one of ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5"].
    :type value: str
    """

    allowed_values = {
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "1.5",
    }
    ONE_ZERO: ClassVar["SpecVersion"]
    ONE_ONE: ClassVar["SpecVersion"]
    ONE_TWO: ClassVar["SpecVersion"]
    ONE_THREE: ClassVar["SpecVersion"]
    ONE_FOUR: ClassVar["SpecVersion"]
    ONE_FIVE: ClassVar["SpecVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SpecVersion.ONE_ZERO = SpecVersion("1.0")
SpecVersion.ONE_ONE = SpecVersion("1.1")
SpecVersion.ONE_TWO = SpecVersion("1.2")
SpecVersion.ONE_THREE = SpecVersion("1.3")
SpecVersion.ONE_FOUR = SpecVersion("1.4")
SpecVersion.ONE_FIVE = SpecVersion("1.5")
