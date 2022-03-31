# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SyntheticsBrowserTestFailureCode(ModelSimple):

    allowed_values = {
        "value": {
            "API_REQUEST_FAILURE": "API_REQUEST_FAILURE",
            "ASSERTION_FAILURE": "ASSERTION_FAILURE",
            "DOWNLOAD_FILE_TOO_LARGE": "DOWNLOAD_FILE_TOO_LARGE",
            "ELEMENT_NOT_INTERACTABLE": "ELEMENT_NOT_INTERACTABLE",
            "EMAIL_VARIABLE_NOT_DEFINED": "EMAIL_VARIABLE_NOT_DEFINED",
            "EVALUATE_JAVASCRIPT": "EVALUATE_JAVASCRIPT",
            "EVALUATE_JAVASCRIPT_CONTEXT": "EVALUATE_JAVASCRIPT_CONTEXT",
            "EXTRACT_VARIABLE": "EXTRACT_VARIABLE",
            "FORBIDDEN_URL": "FORBIDDEN_URL",
            "FRAME_DETACHED": "FRAME_DETACHED",
            "INCONSISTENCIES": "INCONSISTENCIES",
            "INTERNAL_ERROR": "INTERNAL_ERROR",
            "INVALID_TYPE_TEXT_DELAY": "INVALID_TYPE_TEXT_DELAY",
            "INVALID_URL": "INVALID_URL",
            "INVALID_VARIABLE_PATTERN": "INVALID_VARIABLE_PATTERN",
            "INVISIBLE_ELEMENT": "INVISIBLE_ELEMENT",
            "LOCATE_ELEMENT": "LOCATE_ELEMENT",
            "NAVIGATE_TO_LINK": "NAVIGATE_TO_LINK",
            "OPEN_URL": "OPEN_URL",
            "PRESS_KEY": "PRESS_KEY",
            "SERVER_CERTIFICATE": "SERVER_CERTIFICATE",
            "SELECT_OPTION": "SELECT_OPTION",
            "STEP_TIMEOUT": "STEP_TIMEOUT",
            "SUB_TEST_NOT_PASSED": "SUB_TEST_NOT_PASSED",
            "TEST_TIMEOUT": "TEST_TIMEOUT",
            "TOO_MANY_HTTP_REQUESTS": "TOO_MANY_HTTP_REQUESTS",
            "UNAVAILABLE_BROWSER": "UNAVAILABLE_BROWSER",
            "UNKNOWN": "UNKNOWN",
            "UNSUPPORTED_AUTH_SCHEMA": "UNSUPPORTED_AUTH_SCHEMA",
            "UPLOAD_FILES_ELEMENT_TYPE": "UPLOAD_FILES_ELEMENT_TYPE",
            "UPLOAD_FILES_DIALOG": "UPLOAD_FILES_DIALOG",
            "UPLOAD_FILES_DYNAMIC_ELEMENT": "UPLOAD_FILES_DYNAMIC_ELEMENT",
            "UPLOAD_FILES_NAME": "UPLOAD_FILES_NAME",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Error code that can be returned by a Synthetic test.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["API_REQUEST_FAILURE", "ASSERTION_FAILURE", "DOWNLOAD_FILE_TOO_LARGE", "ELEMENT_NOT_INTERACTABLE", "EMAIL_VARIABLE_NOT_DEFINED", "EVALUATE_JAVASCRIPT", "EVALUATE_JAVASCRIPT_CONTEXT", "EXTRACT_VARIABLE", "FORBIDDEN_URL", "FRAME_DETACHED", "INCONSISTENCIES", "INTERNAL_ERROR", "INVALID_TYPE_TEXT_DELAY", "INVALID_URL", "INVALID_VARIABLE_PATTERN", "INVISIBLE_ELEMENT", "LOCATE_ELEMENT", "NAVIGATE_TO_LINK", "OPEN_URL", "PRESS_KEY", "SERVER_CERTIFICATE", "SELECT_OPTION", "STEP_TIMEOUT", "SUB_TEST_NOT_PASSED", "TEST_TIMEOUT", "TOO_MANY_HTTP_REQUESTS", "UNAVAILABLE_BROWSER", "UNKNOWN", "UNSUPPORTED_AUTH_SCHEMA", "UPLOAD_FILES_ELEMENT_TYPE", "UPLOAD_FILES_DIALOG", "UPLOAD_FILES_DYNAMIC_ELEMENT", "UPLOAD_FILES_NAME"].
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
