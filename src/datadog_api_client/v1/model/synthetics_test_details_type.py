# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestDetailsType(ModelSimple):
    """
    Type of the Synthetic test.

    :param value: Must be one of ["api", "browser", "mobile", "network"].
    :type value: str
    """

    allowed_values = {
        "api",
        "browser",
        "mobile",
        "network",
    }
    API: ClassVar["SyntheticsTestDetailsType"]
    BROWSER: ClassVar["SyntheticsTestDetailsType"]
    MOBILE: ClassVar["SyntheticsTestDetailsType"]
    NETWORK: ClassVar["SyntheticsTestDetailsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestDetailsType.API = SyntheticsTestDetailsType("api")
SyntheticsTestDetailsType.BROWSER = SyntheticsTestDetailsType("browser")
SyntheticsTestDetailsType.MOBILE = SyntheticsTestDetailsType("mobile")
SyntheticsTestDetailsType.NETWORK = SyntheticsTestDetailsType("network")
