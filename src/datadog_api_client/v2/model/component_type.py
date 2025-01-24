# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ComponentType(ModelSimple):
    """
    The UI component type.

    :param value: Must be one of ["table", "textInput", "textArea", "button", "text", "select", "modal", "schemaForm", "checkbox", "tabs", "vegaChart", "radioButtons", "numberInput", "fileInput", "jsonInput", "gridCell", "dateRangePicker", "search", "container", "calloutValue"].
    :type value: str
    """

    allowed_values = {
        "table",
        "textInput",
        "textArea",
        "button",
        "text",
        "select",
        "modal",
        "schemaForm",
        "checkbox",
        "tabs",
        "vegaChart",
        "radioButtons",
        "numberInput",
        "fileInput",
        "jsonInput",
        "gridCell",
        "dateRangePicker",
        "search",
        "container",
        "calloutValue",
    }
    TABLE: ClassVar["ComponentType"]
    TEXTINPUT: ClassVar["ComponentType"]
    TEXTAREA: ClassVar["ComponentType"]
    BUTTON: ClassVar["ComponentType"]
    TEXT: ClassVar["ComponentType"]
    SELECT: ClassVar["ComponentType"]
    MODAL: ClassVar["ComponentType"]
    SCHEMAFORM: ClassVar["ComponentType"]
    CHECKBOX: ClassVar["ComponentType"]
    TABS: ClassVar["ComponentType"]
    VEGACHART: ClassVar["ComponentType"]
    RADIOBUTTONS: ClassVar["ComponentType"]
    NUMBERINPUT: ClassVar["ComponentType"]
    FILEINPUT: ClassVar["ComponentType"]
    JSONINPUT: ClassVar["ComponentType"]
    GRIDCELL: ClassVar["ComponentType"]
    DATERANGEPICKER: ClassVar["ComponentType"]
    SEARCH: ClassVar["ComponentType"]
    CONTAINER: ClassVar["ComponentType"]
    CALLOUTVALUE: ClassVar["ComponentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ComponentType.TABLE = ComponentType("table")
ComponentType.TEXTINPUT = ComponentType("textInput")
ComponentType.TEXTAREA = ComponentType("textArea")
ComponentType.BUTTON = ComponentType("button")
ComponentType.TEXT = ComponentType("text")
ComponentType.SELECT = ComponentType("select")
ComponentType.MODAL = ComponentType("modal")
ComponentType.SCHEMAFORM = ComponentType("schemaForm")
ComponentType.CHECKBOX = ComponentType("checkbox")
ComponentType.TABS = ComponentType("tabs")
ComponentType.VEGACHART = ComponentType("vegaChart")
ComponentType.RADIOBUTTONS = ComponentType("radioButtons")
ComponentType.NUMBERINPUT = ComponentType("numberInput")
ComponentType.FILEINPUT = ComponentType("fileInput")
ComponentType.JSONINPUT = ComponentType("jsonInput")
ComponentType.GRIDCELL = ComponentType("gridCell")
ComponentType.DATERANGEPICKER = ComponentType("dateRangePicker")
ComponentType.SEARCH = ComponentType("search")
ComponentType.CONTAINER = ComponentType("container")
ComponentType.CALLOUTVALUE = ComponentType("calloutValue")
