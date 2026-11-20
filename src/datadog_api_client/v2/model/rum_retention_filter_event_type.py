# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMRetentionFilterEventType(ModelSimple):
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
    SESSION: ClassVar["RUMRetentionFilterEventType"]
    VIEW: ClassVar["RUMRetentionFilterEventType"]
    ACTION: ClassVar["RUMRetentionFilterEventType"]
    ERROR: ClassVar["RUMRetentionFilterEventType"]
    RESOURCE: ClassVar["RUMRetentionFilterEventType"]
    LONG_TASK: ClassVar["RUMRetentionFilterEventType"]
    VITAL: ClassVar["RUMRetentionFilterEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMRetentionFilterEventType.SESSION = RUMRetentionFilterEventType("session")
RUMRetentionFilterEventType.VIEW = RUMRetentionFilterEventType("view")
RUMRetentionFilterEventType.ACTION = RUMRetentionFilterEventType("action")
RUMRetentionFilterEventType.ERROR = RUMRetentionFilterEventType("error")
RUMRetentionFilterEventType.RESOURCE = RUMRetentionFilterEventType("resource")
RUMRetentionFilterEventType.LONG_TASK = RUMRetentionFilterEventType("long_task")
RUMRetentionFilterEventType.VITAL = RUMRetentionFilterEventType("vital")
