# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsStepType(ModelSimple):
    """
    Step type used in your Synthetic test.

    :param value: Must be one of ["assertCurrentUrl", "assertElementAttribute", "assertElementContent", "assertElementPresent", "assertEmail", "assertFileDownload", "assertFromJavascript", "assertPageContains", "assertPageLacks", "click", "extractFromJavascript", "extractVariable", "goToEmailLink", "goToUrl", "goToUrlAndMeasureTti", "hover", "playSubTest", "pressKey", "refresh", "runApiTest", "scroll", "selectOption", "typeText", "uploadFiles", "wait"].
    :type value: str
    """

    allowed_values = {
        "assertCurrentUrl",
        "assertElementAttribute",
        "assertElementContent",
        "assertElementPresent",
        "assertEmail",
        "assertFileDownload",
        "assertFromJavascript",
        "assertPageContains",
        "assertPageLacks",
        "click",
        "extractFromJavascript",
        "extractVariable",
        "goToEmailLink",
        "goToUrl",
        "goToUrlAndMeasureTti",
        "hover",
        "playSubTest",
        "pressKey",
        "refresh",
        "runApiTest",
        "scroll",
        "selectOption",
        "typeText",
        "uploadFiles",
        "wait",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsStepType.ASSERT_CURRENT_URL = SyntheticsStepType("assertCurrentUrl")
SyntheticsStepType.ASSERT_ELEMENT_ATTRIBUTE = SyntheticsStepType("assertElementAttribute")
SyntheticsStepType.ASSERT_ELEMENT_CONTENT = SyntheticsStepType("assertElementContent")
SyntheticsStepType.ASSERT_ELEMENT_PRESENT = SyntheticsStepType("assertElementPresent")
SyntheticsStepType.ASSERT_EMAIL = SyntheticsStepType("assertEmail")
SyntheticsStepType.ASSERT_FILE_DOWNLOAD = SyntheticsStepType("assertFileDownload")
SyntheticsStepType.ASSERT_FROM_JAVASCRIPT = SyntheticsStepType("assertFromJavascript")
SyntheticsStepType.ASSERT_PAGE_CONTAINS = SyntheticsStepType("assertPageContains")
SyntheticsStepType.ASSERT_PAGE_LACKS = SyntheticsStepType("assertPageLacks")
SyntheticsStepType.CLICK = SyntheticsStepType("click")
SyntheticsStepType.EXTRACT_FROM_JAVASCRIPT = SyntheticsStepType("extractFromJavascript")
SyntheticsStepType.EXTRACT_VARIABLE = SyntheticsStepType("extractVariable")
SyntheticsStepType.GO_TO_EMAIL_LINK = SyntheticsStepType("goToEmailLink")
SyntheticsStepType.GO_TO_URL = SyntheticsStepType("goToUrl")
SyntheticsStepType.GO_TO_URL_AND_MEASURE_TTI = SyntheticsStepType("goToUrlAndMeasureTti")
SyntheticsStepType.HOVER = SyntheticsStepType("hover")
SyntheticsStepType.PLAY_SUB_TEST = SyntheticsStepType("playSubTest")
SyntheticsStepType.PRESS_KEY = SyntheticsStepType("pressKey")
SyntheticsStepType.REFRESH = SyntheticsStepType("refresh")
SyntheticsStepType.RUN_API_TEST = SyntheticsStepType("runApiTest")
SyntheticsStepType.SCROLL = SyntheticsStepType("scroll")
SyntheticsStepType.SELECT_OPTION = SyntheticsStepType("selectOption")
SyntheticsStepType.TYPE_TEXT = SyntheticsStepType("typeText")
SyntheticsStepType.UPLOAD_FILES = SyntheticsStepType("uploadFiles")
SyntheticsStepType.WAIT = SyntheticsStepType("wait")
