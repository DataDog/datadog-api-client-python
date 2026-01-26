# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestOptionsMonitorOptionsNotificationPresetName(ModelSimple):
    """
    The name of the preset for the notification for the monitor.

    :param value: Must be one of ["show_all", "hide_all", "hide_query", "hide_handles", "hide_query_and_handles", "show_only_snapshot", "hide_handles_and_footer"].
    :type value: str
    """

    allowed_values = {
        "show_all",
        "hide_all",
        "hide_query",
        "hide_handles",
        "hide_query_and_handles",
        "show_only_snapshot",
        "hide_handles_and_footer",
    }
    SHOW_ALL: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_ALL: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_QUERY: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_HANDLES: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_QUERY_AND_HANDLES: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]
    SHOW_ONLY_SNAPSHOT: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_HANDLES_AND_FOOTER: ClassVar["SyntheticsTestOptionsMonitorOptionsNotificationPresetName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestOptionsMonitorOptionsNotificationPresetName.SHOW_ALL = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("show_all")
)
SyntheticsTestOptionsMonitorOptionsNotificationPresetName.HIDE_ALL = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("hide_all")
)
SyntheticsTestOptionsMonitorOptionsNotificationPresetName.HIDE_QUERY = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("hide_query")
)
SyntheticsTestOptionsMonitorOptionsNotificationPresetName.HIDE_HANDLES = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("hide_handles")
)
SyntheticsTestOptionsMonitorOptionsNotificationPresetName.HIDE_QUERY_AND_HANDLES = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("hide_query_and_handles")
)
SyntheticsTestOptionsMonitorOptionsNotificationPresetName.SHOW_ONLY_SNAPSHOT = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("show_only_snapshot")
)
SyntheticsTestOptionsMonitorOptionsNotificationPresetName.HIDE_HANDLES_AND_FOOTER = (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName("hide_handles_and_footer")
)
