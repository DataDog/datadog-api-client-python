# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipOwnerType(ModelSimple):
    """
    The owner type for an ownership inference.

    :param value: Must be one of ["user", "team", "service", "unknown"].
    :type value: str
    """

    allowed_values = {
        "user",
        "team",
        "service",
        "unknown",
    }
    USER: ClassVar["OwnershipOwnerType"]
    TEAM: ClassVar["OwnershipOwnerType"]
    SERVICE: ClassVar["OwnershipOwnerType"]
    UNKNOWN: ClassVar["OwnershipOwnerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipOwnerType.USER = OwnershipOwnerType("user")
OwnershipOwnerType.TEAM = OwnershipOwnerType("team")
OwnershipOwnerType.SERVICE = OwnershipOwnerType("service")
OwnershipOwnerType.UNKNOWN = OwnershipOwnerType("unknown")
