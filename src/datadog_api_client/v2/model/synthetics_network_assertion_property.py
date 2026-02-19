# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkAssertionProperty(ModelSimple):
    """
    The associated assertion property.

    :param value: Must be one of ["avg", "max", "min"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "max",
        "min",
    }
    AVG: ClassVar["SyntheticsNetworkAssertionProperty"]
    MAX: ClassVar["SyntheticsNetworkAssertionProperty"]
    MIN: ClassVar["SyntheticsNetworkAssertionProperty"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkAssertionProperty.AVG = SyntheticsNetworkAssertionProperty("avg")
SyntheticsNetworkAssertionProperty.MAX = SyntheticsNetworkAssertionProperty("max")
SyntheticsNetworkAssertionProperty.MIN = SyntheticsNetworkAssertionProperty("min")
