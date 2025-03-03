# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterEventType(ModelSimple):
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
    SESSION: ClassVar["RumRetentionFilterEventType"]
    VIEW: ClassVar["RumRetentionFilterEventType"]
    ACTION: ClassVar["RumRetentionFilterEventType"]
    ERROR: ClassVar["RumRetentionFilterEventType"]
    RESOURCE: ClassVar["RumRetentionFilterEventType"]
    LONG_TASK: ClassVar["RumRetentionFilterEventType"]
    VITAL: ClassVar["RumRetentionFilterEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterEventType.SESSION = RumRetentionFilterEventType("session")
RumRetentionFilterEventType.VIEW = RumRetentionFilterEventType("view")
RumRetentionFilterEventType.ACTION = RumRetentionFilterEventType("action")
RumRetentionFilterEventType.ERROR = RumRetentionFilterEventType("error")
RumRetentionFilterEventType.RESOURCE = RumRetentionFilterEventType("resource")
RumRetentionFilterEventType.LONG_TASK = RumRetentionFilterEventType("long_task")
RumRetentionFilterEventType.VITAL = RumRetentionFilterEventType("vital")
