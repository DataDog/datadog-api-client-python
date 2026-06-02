# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumHardcodedRetentionFilterEventType(ModelSimple):
    """
    The type of RUM events the hardcoded filter applies to. Read-only.

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
    SESSION: ClassVar["RumHardcodedRetentionFilterEventType"]
    VIEW: ClassVar["RumHardcodedRetentionFilterEventType"]
    ACTION: ClassVar["RumHardcodedRetentionFilterEventType"]
    ERROR: ClassVar["RumHardcodedRetentionFilterEventType"]
    RESOURCE: ClassVar["RumHardcodedRetentionFilterEventType"]
    LONG_TASK: ClassVar["RumHardcodedRetentionFilterEventType"]
    VITAL: ClassVar["RumHardcodedRetentionFilterEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumHardcodedRetentionFilterEventType.SESSION = RumHardcodedRetentionFilterEventType("session")
RumHardcodedRetentionFilterEventType.VIEW = RumHardcodedRetentionFilterEventType("view")
RumHardcodedRetentionFilterEventType.ACTION = RumHardcodedRetentionFilterEventType("action")
RumHardcodedRetentionFilterEventType.ERROR = RumHardcodedRetentionFilterEventType("error")
RumHardcodedRetentionFilterEventType.RESOURCE = RumHardcodedRetentionFilterEventType("resource")
RumHardcodedRetentionFilterEventType.LONG_TASK = RumHardcodedRetentionFilterEventType("long_task")
RumHardcodedRetentionFilterEventType.VITAL = RumHardcodedRetentionFilterEventType("vital")
