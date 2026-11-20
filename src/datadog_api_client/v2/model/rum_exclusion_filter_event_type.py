# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMExclusionFilterEventType(ModelSimple):
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
    SESSION: ClassVar["RUMExclusionFilterEventType"]
    VIEW: ClassVar["RUMExclusionFilterEventType"]
    ACTION: ClassVar["RUMExclusionFilterEventType"]
    ERROR: ClassVar["RUMExclusionFilterEventType"]
    RESOURCE: ClassVar["RUMExclusionFilterEventType"]
    LONG_TASK: ClassVar["RUMExclusionFilterEventType"]
    VITAL: ClassVar["RUMExclusionFilterEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMExclusionFilterEventType.SESSION = RUMExclusionFilterEventType("session")
RUMExclusionFilterEventType.VIEW = RUMExclusionFilterEventType("view")
RUMExclusionFilterEventType.ACTION = RUMExclusionFilterEventType("action")
RUMExclusionFilterEventType.ERROR = RUMExclusionFilterEventType("error")
RUMExclusionFilterEventType.RESOURCE = RUMExclusionFilterEventType("resource")
RUMExclusionFilterEventType.LONG_TASK = RUMExclusionFilterEventType("long_task")
RUMExclusionFilterEventType.VITAL = RUMExclusionFilterEventType("vital")
