# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SyntheticsStepType(ModelSimple):

    allowed_values = {
        "value": {
            "ASSERT_CURRENT_URL": "assertCurrentUrl",
            "ASSERT_ELEMENT_ATTRIBUTE": "assertElementAttribute",
            "ASSERT_ELEMENT_CONTENT": "assertElementContent",
            "ASSERT_ELEMENT_PRESENT": "assertElementPresent",
            "ASSERT_EMAIL": "assertEmail",
            "ASSERT_FILE_DOWNLOAD": "assertFileDownload",
            "ASSERT_FROM_JAVASCRIPT": "assertFromJavascript",
            "ASSERT_PAGE_CONTAINS": "assertPageContains",
            "ASSERT_PAGE_LACKS": "assertPageLacks",
            "CLICK": "click",
            "EXTRACT_FROM_JAVASCRIPT": "extractFromJavascript",
            "EXTRACT_VARIABLE": "extractVariable",
            "GO_TO_EMAIL_LINK": "goToEmailLink",
            "GO_TO_URL": "goToUrl",
            "GO_TO_URL_AND_MEASURE_TTI": "goToUrlAndMeasureTti",
            "HOVER": "hover",
            "PLAY_SUB_TEST": "playSubTest",
            "PRESS_KEY": "pressKey",
            "REFRESH": "refresh",
            "RUN_API_TEST": "runApiTest",
            "SCROLL": "scroll",
            "SELECT_OPTION": "selectOption",
            "TYPE_TEXT": "typeText",
            "UPLOAD_FILES": "uploadFiles",
            "WAIT": "wait",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Step type used in your Synthetic test.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["assertCurrentUrl", "assertElementAttribute", "assertElementContent", "assertElementPresent", "assertEmail", "assertFileDownload", "assertFromJavascript", "assertPageContains", "assertPageLacks", "click", "extractFromJavascript", "extractVariable", "goToEmailLink", "goToUrl", "goToUrlAndMeasureTti", "hover", "playSubTest", "pressKey", "refresh", "runApiTest", "scroll", "selectOption", "typeText", "uploadFiles", "wait"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
