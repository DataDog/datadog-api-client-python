# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SyntheticsTestDetailsType(StringEnum):
    """
    Type of the Synthetic test, either `api` or `browser`.

    :param value: Must be one of ["api", "browser"].
    :type value: str
    """

    allowed_values = {
        "api",
        "browser",
    }
    API: ClassVar["SyntheticsTestDetailsType"]
    BROWSER: ClassVar["SyntheticsTestDetailsType"]


SyntheticsTestDetailsType.API = SyntheticsTestDetailsType("api")
SyntheticsTestDetailsType.BROWSER = SyntheticsTestDetailsType("browser")
