# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumMetricEventType(ModelSimple):
    """
    The type of RUM events to filter on.

    :param value: Must be one of ["session", "view", "action", "error", "resource", "long_task", "vital"].
    :type value: str
    """

    allowed_values = {
        "session",
        "view",
        "action",
        "error",
        "resource",
        "long_task",
        "vital",
    }
    SESSION: ClassVar["RumMetricEventType"]
    VIEW: ClassVar["RumMetricEventType"]
    ACTION: ClassVar["RumMetricEventType"]
    ERROR: ClassVar["RumMetricEventType"]
    RESOURCE: ClassVar["RumMetricEventType"]
    LONG_TASK: ClassVar["RumMetricEventType"]
    VITAL: ClassVar["RumMetricEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumMetricEventType.SESSION = RumMetricEventType("session")
RumMetricEventType.VIEW = RumMetricEventType("view")
RumMetricEventType.ACTION = RumMetricEventType("action")
RumMetricEventType.ERROR = RumMetricEventType("error")
RumMetricEventType.RESOURCE = RumMetricEventType("resource")
RumMetricEventType.LONG_TASK = RumMetricEventType("long_task")
RumMetricEventType.VITAL = RumMetricEventType("vital")
