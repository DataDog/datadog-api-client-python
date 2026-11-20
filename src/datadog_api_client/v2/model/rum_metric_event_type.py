# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMMetricEventType(ModelSimple):
    """
    The type of RUM events the metric is generated from. It is set at creation and cannot be changed.

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
    SESSION: ClassVar["RUMMetricEventType"]
    VIEW: ClassVar["RUMMetricEventType"]
    ACTION: ClassVar["RUMMetricEventType"]
    ERROR: ClassVar["RUMMetricEventType"]
    RESOURCE: ClassVar["RUMMetricEventType"]
    LONG_TASK: ClassVar["RUMMetricEventType"]
    VITAL: ClassVar["RUMMetricEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMMetricEventType.SESSION = RUMMetricEventType("session")
RUMMetricEventType.VIEW = RUMMetricEventType("view")
RUMMetricEventType.ACTION = RUMMetricEventType("action")
RUMMetricEventType.ERROR = RUMMetricEventType("error")
RUMMetricEventType.RESOURCE = RUMMetricEventType("resource")
RUMMetricEventType.LONG_TASK = RUMMetricEventType("long_task")
RUMMetricEventType.VITAL = RUMMetricEventType("vital")
