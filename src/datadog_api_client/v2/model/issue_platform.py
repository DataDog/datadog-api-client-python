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
    Platform associated with the issue

    :param value: Must be one of ["browser", "android", "backend", "ios", "react_native", "flutter", "roku"].
    :type value: str
    """

    allowed_values = {
        "browser",
        "android",
        "backend",
        "ios",
        "react_native",
        "flutter",
        "roku",
    }
    BROWSER: ClassVar["IssuePlatform"]
    ANDROID: ClassVar["IssuePlatform"]
    BACKEND: ClassVar["IssuePlatform"]
    IOS: ClassVar["IssuePlatform"]
    REACT_NATIVE: ClassVar["IssuePlatform"]
    FLUTTER: ClassVar["IssuePlatform"]
    ROKU: ClassVar["IssuePlatform"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuePlatform.BROWSER = IssuePlatform("browser")
IssuePlatform.ANDROID = IssuePlatform("android")
IssuePlatform.BACKEND = IssuePlatform("backend")
IssuePlatform.IOS = IssuePlatform("ios")
IssuePlatform.REACT_NATIVE = IssuePlatform("react_native")
IssuePlatform.FLUTTER = IssuePlatform("flutter")
IssuePlatform.ROKU = IssuePlatform("roku")
