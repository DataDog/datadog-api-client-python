# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppBuilderEventType(ModelSimple):
    """
    The response to the event.

    :param value: Must be one of ["custom", "setComponentState", "triggerQuery", "openModal", "closeModal", "openUrl", "downloadFile", "setStateVariableValue"].
    :type value: str
    """

    allowed_values = {
        "custom",
        "setComponentState",
        "triggerQuery",
        "openModal",
        "closeModal",
        "openUrl",
        "downloadFile",
        "setStateVariableValue",
    }
    CUSTOM: ClassVar["AppBuilderEventType"]
    SETCOMPONENTSTATE: ClassVar["AppBuilderEventType"]
    TRIGGERQUERY: ClassVar["AppBuilderEventType"]
    OPENMODAL: ClassVar["AppBuilderEventType"]
    CLOSEMODAL: ClassVar["AppBuilderEventType"]
    OPENURL: ClassVar["AppBuilderEventType"]
    DOWNLOADFILE: ClassVar["AppBuilderEventType"]
    SETSTATEVARIABLEVALUE: ClassVar["AppBuilderEventType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppBuilderEventType.CUSTOM = AppBuilderEventType("custom")
AppBuilderEventType.SETCOMPONENTSTATE = AppBuilderEventType("setComponentState")
AppBuilderEventType.TRIGGERQUERY = AppBuilderEventType("triggerQuery")
AppBuilderEventType.OPENMODAL = AppBuilderEventType("openModal")
AppBuilderEventType.CLOSEMODAL = AppBuilderEventType("closeModal")
AppBuilderEventType.OPENURL = AppBuilderEventType("openUrl")
AppBuilderEventType.DOWNLOADFILE = AppBuilderEventType("downloadFile")
AppBuilderEventType.SETSTATEVARIABLEVALUE = AppBuilderEventType("setStateVariableValue")
