# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumExclusionFilterEventType(ModelSimple):
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
    SESSION: ClassVar["RumExclusionFilterEventType"]
    VIEW: ClassVar["RumExclusionFilterEventType"]
    ACTION: ClassVar["RumExclusionFilterEventType"]
    ERROR: ClassVar["RumExclusionFilterEventType"]
    RESOURCE: ClassVar["RumExclusionFilterEventType"]
    LONG_TASK: ClassVar["RumExclusionFilterEventType"]
    VITAL: ClassVar["RumExclusionFilterEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumExclusionFilterEventType.SESSION = RumExclusionFilterEventType("session")
RumExclusionFilterEventType.VIEW = RumExclusionFilterEventType("view")
RumExclusionFilterEventType.ACTION = RumExclusionFilterEventType("action")
RumExclusionFilterEventType.ERROR = RumExclusionFilterEventType("error")
RumExclusionFilterEventType.RESOURCE = RumExclusionFilterEventType("resource")
RumExclusionFilterEventType.LONG_TASK = RumExclusionFilterEventType("long_task")
RumExclusionFilterEventType.VITAL = RumExclusionFilterEventType("vital")
