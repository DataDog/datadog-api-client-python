# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestType(ModelSimple):
    """
    Type of the Synthetic test that produced this result.

    :param value: Must be one of ["api", "browser", "mobile", "network"].
    :type value: str
    """

    allowed_values = {
        "api",
        "browser",
        "mobile",
        "network",
    }
    API: ClassVar["SyntheticsTestType"]
    BROWSER: ClassVar["SyntheticsTestType"]
    MOBILE: ClassVar["SyntheticsTestType"]
    NETWORK: ClassVar["SyntheticsTestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestType.API = SyntheticsTestType("api")
SyntheticsTestType.BROWSER = SyntheticsTestType("browser")
SyntheticsTestType.MOBILE = SyntheticsTestType("mobile")
SyntheticsTestType.NETWORK = SyntheticsTestType("network")
