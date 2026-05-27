# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumPermanentRetentionFilterEventType(ModelSimple):
    """
    The type of RUM events the filter applies to. Read-only.

    :param value: Must be one of ["session", "view", "action", "error", "resource", "long_task", "vital", "operation"].
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
        "operation",
    }
    SESSION: ClassVar["RumPermanentRetentionFilterEventType"]
    VIEW: ClassVar["RumPermanentRetentionFilterEventType"]
    ACTION: ClassVar["RumPermanentRetentionFilterEventType"]
    ERROR: ClassVar["RumPermanentRetentionFilterEventType"]
    RESOURCE: ClassVar["RumPermanentRetentionFilterEventType"]
    LONG_TASK: ClassVar["RumPermanentRetentionFilterEventType"]
    VITAL: ClassVar["RumPermanentRetentionFilterEventType"]
    OPERATION: ClassVar["RumPermanentRetentionFilterEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumPermanentRetentionFilterEventType.SESSION = RumPermanentRetentionFilterEventType("session")
RumPermanentRetentionFilterEventType.VIEW = RumPermanentRetentionFilterEventType("view")
RumPermanentRetentionFilterEventType.ACTION = RumPermanentRetentionFilterEventType("action")
RumPermanentRetentionFilterEventType.ERROR = RumPermanentRetentionFilterEventType("error")
RumPermanentRetentionFilterEventType.RESOURCE = RumPermanentRetentionFilterEventType("resource")
RumPermanentRetentionFilterEventType.LONG_TASK = RumPermanentRetentionFilterEventType("long_task")
RumPermanentRetentionFilterEventType.VITAL = RumPermanentRetentionFilterEventType("vital")
RumPermanentRetentionFilterEventType.OPERATION = RumPermanentRetentionFilterEventType("operation")
