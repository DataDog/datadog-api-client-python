# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorUserTemplateResourceType(ModelSimple):
    """
    Monitor user template resource type.

    :param value: If omitted defaults to "monitor-user-template". Must be one of ["monitor-user-template"].
    :type value: str
    """

    allowed_values = {
        "monitor-user-template",
    }
    MONITOR_USER_TEMPLATE: ClassVar["MonitorUserTemplateResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE = MonitorUserTemplateResourceType("monitor-user-template")
