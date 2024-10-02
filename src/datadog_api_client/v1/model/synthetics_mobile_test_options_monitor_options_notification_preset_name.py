# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName(ModelSimple):
    """
    The definition of `SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName` object.

    :param value: Must be one of ["show_all", "hide_all", "hide_query", "hide_handles"].
    :type value: str
    """

    allowed_values = {
        "show_all",
        "hide_all",
        "hide_query",
        "hide_handles",
    }
    SHOW_ALL: ClassVar["SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_ALL: ClassVar["SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_QUERY: ClassVar["SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName"]
    HIDE_HANDLES: ClassVar["SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName.SHOW_ALL = (
    SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName("show_all")
)
SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName.HIDE_ALL = (
    SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName("hide_all")
)
SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName.HIDE_QUERY = (
    SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName("hide_query")
)
SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName.HIDE_HANDLES = (
    SyntheticsMobileTestOptionsMonitorOptionsNotificationPresetName("hide_handles")
)
