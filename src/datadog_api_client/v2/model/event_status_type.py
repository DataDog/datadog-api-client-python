# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventStatusType(ModelSimple):
    """
    The event status. Legacy events can use `failure`, `error`, `warning`,
        `info`, `success`, `user_update`, `recommendation`, or `snapshot`.
        Alert events can use `error`, `warn`, or `ok`.

    :param value: Must be one of ["failure", "error", "warn", "warning", "ok", "info", "success", "user_update", "recommendation", "snapshot"].
    :type value: str
    """

    allowed_values = {
        "failure",
        "error",
        "warn",
        "warning",
        "ok",
        "info",
        "success",
        "user_update",
        "recommendation",
        "snapshot",
    }
    FAILURE: ClassVar["EventStatusType"]
    ERROR: ClassVar["EventStatusType"]
    WARN: ClassVar["EventStatusType"]
    WARNING: ClassVar["EventStatusType"]
    OK: ClassVar["EventStatusType"]
    INFO: ClassVar["EventStatusType"]
    SUCCESS: ClassVar["EventStatusType"]
    USER_UPDATE: ClassVar["EventStatusType"]
    RECOMMENDATION: ClassVar["EventStatusType"]
    SNAPSHOT: ClassVar["EventStatusType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventStatusType.FAILURE = EventStatusType("failure")
EventStatusType.ERROR = EventStatusType("error")
EventStatusType.WARN = EventStatusType("warn")
EventStatusType.WARNING = EventStatusType("warning")
EventStatusType.OK = EventStatusType("ok")
EventStatusType.INFO = EventStatusType("info")
EventStatusType.SUCCESS = EventStatusType("success")
EventStatusType.USER_UPDATE = EventStatusType("user_update")
EventStatusType.RECOMMENDATION = EventStatusType("recommendation")
EventStatusType.SNAPSHOT = EventStatusType("snapshot")
