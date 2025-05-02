# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UserAttributesStatus(ModelSimple):
    """
    The user's status.

    :param value: Must be one of ["active", "deactivated", "pending"].
    :type value: str
    """

    allowed_values = {
        "active",
        "deactivated",
        "pending",
    }
    ACTIVE: ClassVar["UserAttributesStatus"]
    DEACTIVATED: ClassVar["UserAttributesStatus"]
    PENDING: ClassVar["UserAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UserAttributesStatus.ACTIVE = UserAttributesStatus("active")
UserAttributesStatus.DEACTIVATED = UserAttributesStatus("deactivated")
UserAttributesStatus.PENDING = UserAttributesStatus("pending")
