# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppBuilderEventName(ModelSimple):
    """
    The triggering action for the event.

    :param value: Must be one of ["pageChange", "tableRowClick", "_tableRowButtonClick", "change", "submit", "click", "toggleOpen", "close", "open", "executionFinished"].
    :type value: str
    """

    allowed_values = {
        "pageChange",
        "tableRowClick",
        "_tableRowButtonClick",
        "change",
        "submit",
        "click",
        "toggleOpen",
        "close",
        "open",
        "executionFinished",
    }
    PAGECHANGE: ClassVar["AppBuilderEventName"]
    TABLEROWCLICK: ClassVar["AppBuilderEventName"]
    TABLEROWBUTTONCLICK: ClassVar["AppBuilderEventName"]
    CHANGE: ClassVar["AppBuilderEventName"]
    SUBMIT: ClassVar["AppBuilderEventName"]
    CLICK: ClassVar["AppBuilderEventName"]
    TOGGLEOPEN: ClassVar["AppBuilderEventName"]
    CLOSE: ClassVar["AppBuilderEventName"]
    OPEN: ClassVar["AppBuilderEventName"]
    EXECUTIONFINISHED: ClassVar["AppBuilderEventName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppBuilderEventName.PAGECHANGE = AppBuilderEventName("pageChange")
AppBuilderEventName.TABLEROWCLICK = AppBuilderEventName("tableRowClick")
AppBuilderEventName.TABLEROWBUTTONCLICK = AppBuilderEventName("_tableRowButtonClick")
AppBuilderEventName.CHANGE = AppBuilderEventName("change")
AppBuilderEventName.SUBMIT = AppBuilderEventName("submit")
AppBuilderEventName.CLICK = AppBuilderEventName("click")
AppBuilderEventName.TOGGLEOPEN = AppBuilderEventName("toggleOpen")
AppBuilderEventName.CLOSE = AppBuilderEventName("close")
AppBuilderEventName.OPEN = AppBuilderEventName("open")
AppBuilderEventName.EXECUTIONFINISHED = AppBuilderEventName("executionFinished")
