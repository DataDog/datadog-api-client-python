# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotifyEndType(ModelSimple):
    """
    A notification end type.

    :param value: Must be one of ["canceled", "expired"].
    :type value: str
    """

    allowed_values = {
        "canceled",
        "expired",
    }
    CANCELED: ClassVar["NotifyEndType"]
    EXPIRED: ClassVar["NotifyEndType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotifyEndType.CANCELED = NotifyEndType("canceled")
NotifyEndType.EXPIRED = NotifyEndType("expired")
