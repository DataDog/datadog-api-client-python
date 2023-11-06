# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SyntheticsAssertionTimingsScope(StringEnum):
    """
    Timings scope for response time assertions.

    :param value: Must be one of ["all", "withoutDNS"].
    :type value: str
    """

    allowed_values = {
        "all",
        "withoutDNS",
    }
    ALL: ClassVar["SyntheticsAssertionTimingsScope"]
    WITHOUT_DNS: ClassVar["SyntheticsAssertionTimingsScope"]


SyntheticsAssertionTimingsScope.ALL = SyntheticsAssertionTimingsScope("all")
SyntheticsAssertionTimingsScope.WITHOUT_DNS = SyntheticsAssertionTimingsScope("withoutDNS")
