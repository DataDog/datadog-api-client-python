# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class CIAppCIErrorDomain(StringEnum):
    """
    Error category used to differentiate between issues related to the developer or provider environments.

    :param value: Must be one of ["provider", "user", "unknown"].
    :type value: str
    """

    allowed_values = {
        "provider",
        "user",
        "unknown",
    }
    PROVIDER: ClassVar["CIAppCIErrorDomain"]
    USER: ClassVar["CIAppCIErrorDomain"]
    UNKNOWN: ClassVar["CIAppCIErrorDomain"]


CIAppCIErrorDomain.PROVIDER = CIAppCIErrorDomain("provider")
CIAppCIErrorDomain.USER = CIAppCIErrorDomain("user")
CIAppCIErrorDomain.UNKNOWN = CIAppCIErrorDomain("unknown")
