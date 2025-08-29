# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuePlatform(ModelSimple):
    """
    Platform associated with the issue.

    :param value: Must be one of ["ANDROID", "BACKEND", "BROWSER", "FLUTTER", "IOS", "REACT_NATIVE", "ROKU", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "ANDROID",
        "BACKEND",
        "BROWSER",
        "FLUTTER",
        "IOS",
        "REACT_NATIVE",
        "ROKU",
        "UNKNOWN",
    }
    ANDROID: ClassVar["IssuePlatform"]
    BACKEND: ClassVar["IssuePlatform"]
    BROWSER: ClassVar["IssuePlatform"]
    FLUTTER: ClassVar["IssuePlatform"]
    IOS: ClassVar["IssuePlatform"]
    REACT_NATIVE: ClassVar["IssuePlatform"]
    ROKU: ClassVar["IssuePlatform"]
    UNKNOWN: ClassVar["IssuePlatform"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuePlatform.ANDROID = IssuePlatform("ANDROID")
IssuePlatform.BACKEND = IssuePlatform("BACKEND")
IssuePlatform.BROWSER = IssuePlatform("BROWSER")
IssuePlatform.FLUTTER = IssuePlatform("FLUTTER")
IssuePlatform.IOS = IssuePlatform("IOS")
IssuePlatform.REACT_NATIVE = IssuePlatform("REACT_NATIVE")
IssuePlatform.ROKU = IssuePlatform("ROKU")
IssuePlatform.UNKNOWN = IssuePlatform("UNKNOWN")
