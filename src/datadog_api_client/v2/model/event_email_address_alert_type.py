# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventEmailAddressAlertType(ModelSimple):
    """
    The alert type of events generated from the email address.

    :param value: Must be one of ["info", "warn", "error", "success"].
    :type value: str
    """

    allowed_values = {
        "info",
        "warn",
        "error",
        "success",
    }
    INFO: ClassVar["EventEmailAddressAlertType"]
    WARN: ClassVar["EventEmailAddressAlertType"]
    ERROR: ClassVar["EventEmailAddressAlertType"]
    SUCCESS: ClassVar["EventEmailAddressAlertType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventEmailAddressAlertType.INFO = EventEmailAddressAlertType("info")
EventEmailAddressAlertType.WARN = EventEmailAddressAlertType("warn")
EventEmailAddressAlertType.ERROR = EventEmailAddressAlertType("error")
EventEmailAddressAlertType.SUCCESS = EventEmailAddressAlertType("success")
