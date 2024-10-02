# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileStepType(ModelSimple):
    """
    Step type used in your mobile Synthetic test.

    :param value: Must be one of ["assertElementContent", "assertScreenContains", "assertScreenLacks", "doubleTap", "extractVariable", "flick", "openDeeplink", "playSubTest", "pressBack", "restartApplication", "rotate", "scroll", "scrollToElement", "tap", "toggleWiFi", "typeText", "wait"].
    :type value: str
    """

    allowed_values = {
        "assertElementContent",
        "assertScreenContains",
        "assertScreenLacks",
        "doubleTap",
        "extractVariable",
        "flick",
        "openDeeplink",
        "playSubTest",
        "pressBack",
        "restartApplication",
        "rotate",
        "scroll",
        "scrollToElement",
        "tap",
        "toggleWiFi",
        "typeText",
        "wait",
    }
    ASSERTELEMENTCONTENT: ClassVar["SyntheticsMobileStepType"]
    ASSERTSCREENCONTAINS: ClassVar["SyntheticsMobileStepType"]
    ASSERTSCREENLACKS: ClassVar["SyntheticsMobileStepType"]
    DOUBLETAP: ClassVar["SyntheticsMobileStepType"]
    EXTRACTVARIABLE: ClassVar["SyntheticsMobileStepType"]
    FLICK: ClassVar["SyntheticsMobileStepType"]
    OPENDEEPLINK: ClassVar["SyntheticsMobileStepType"]
    PLAYSUBTEST: ClassVar["SyntheticsMobileStepType"]
    PRESSBACK: ClassVar["SyntheticsMobileStepType"]
    RESTARTAPPLICATION: ClassVar["SyntheticsMobileStepType"]
    ROTATE: ClassVar["SyntheticsMobileStepType"]
    SCROLL: ClassVar["SyntheticsMobileStepType"]
    SCROLLTOELEMENT: ClassVar["SyntheticsMobileStepType"]
    TAP: ClassVar["SyntheticsMobileStepType"]
    TOGGLEWIFI: ClassVar["SyntheticsMobileStepType"]
    TYPETEXT: ClassVar["SyntheticsMobileStepType"]
    WAIT: ClassVar["SyntheticsMobileStepType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileStepType.ASSERTELEMENTCONTENT = SyntheticsMobileStepType("assertElementContent")
SyntheticsMobileStepType.ASSERTSCREENCONTAINS = SyntheticsMobileStepType("assertScreenContains")
SyntheticsMobileStepType.ASSERTSCREENLACKS = SyntheticsMobileStepType("assertScreenLacks")
SyntheticsMobileStepType.DOUBLETAP = SyntheticsMobileStepType("doubleTap")
SyntheticsMobileStepType.EXTRACTVARIABLE = SyntheticsMobileStepType("extractVariable")
SyntheticsMobileStepType.FLICK = SyntheticsMobileStepType("flick")
SyntheticsMobileStepType.OPENDEEPLINK = SyntheticsMobileStepType("openDeeplink")
SyntheticsMobileStepType.PLAYSUBTEST = SyntheticsMobileStepType("playSubTest")
SyntheticsMobileStepType.PRESSBACK = SyntheticsMobileStepType("pressBack")
SyntheticsMobileStepType.RESTARTAPPLICATION = SyntheticsMobileStepType("restartApplication")
SyntheticsMobileStepType.ROTATE = SyntheticsMobileStepType("rotate")
SyntheticsMobileStepType.SCROLL = SyntheticsMobileStepType("scroll")
SyntheticsMobileStepType.SCROLLTOELEMENT = SyntheticsMobileStepType("scrollToElement")
SyntheticsMobileStepType.TAP = SyntheticsMobileStepType("tap")
SyntheticsMobileStepType.TOGGLEWIFI = SyntheticsMobileStepType("toggleWiFi")
SyntheticsMobileStepType.TYPETEXT = SyntheticsMobileStepType("typeText")
SyntheticsMobileStepType.WAIT = SyntheticsMobileStepType("wait")
