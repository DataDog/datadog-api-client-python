# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMApplicationPlatformType(ModelSimple):
    """
    Type of the RUM application, that is the platform of the RUM SDK. Defaults to `browser` on create.

    :param value: Must be one of ["browser", "ios", "android", "react-native", "flutter", "roku", "electron", "unity", "kotlin-multiplatform", "react", "nextjs", "angular", "vuejs", "nuxt", "tanstack", "maui", "salesforce-lwc", "shopify", "cpp", "unreal"].
    :type value: str
    """

    allowed_values = {
        "browser",
        "ios",
        "android",
        "react-native",
        "flutter",
        "roku",
        "electron",
        "unity",
        "kotlin-multiplatform",
        "react",
        "nextjs",
        "angular",
        "vuejs",
        "nuxt",
        "tanstack",
        "maui",
        "salesforce-lwc",
        "shopify",
        "cpp",
        "unreal",
    }
    BROWSER: ClassVar["RUMApplicationPlatformType"]
    IOS: ClassVar["RUMApplicationPlatformType"]
    ANDROID: ClassVar["RUMApplicationPlatformType"]
    REACT_NATIVE: ClassVar["RUMApplicationPlatformType"]
    FLUTTER: ClassVar["RUMApplicationPlatformType"]
    ROKU: ClassVar["RUMApplicationPlatformType"]
    ELECTRON: ClassVar["RUMApplicationPlatformType"]
    UNITY: ClassVar["RUMApplicationPlatformType"]
    KOTLIN_MULTIPLATFORM: ClassVar["RUMApplicationPlatformType"]
    REACT: ClassVar["RUMApplicationPlatformType"]
    NEXTJS: ClassVar["RUMApplicationPlatformType"]
    ANGULAR: ClassVar["RUMApplicationPlatformType"]
    VUEJS: ClassVar["RUMApplicationPlatformType"]
    NUXT: ClassVar["RUMApplicationPlatformType"]
    TANSTACK: ClassVar["RUMApplicationPlatformType"]
    MAUI: ClassVar["RUMApplicationPlatformType"]
    SALESFORCE_LWC: ClassVar["RUMApplicationPlatformType"]
    SHOPIFY: ClassVar["RUMApplicationPlatformType"]
    CPP: ClassVar["RUMApplicationPlatformType"]
    UNREAL: ClassVar["RUMApplicationPlatformType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMApplicationPlatformType.BROWSER = RUMApplicationPlatformType("browser")
RUMApplicationPlatformType.IOS = RUMApplicationPlatformType("ios")
RUMApplicationPlatformType.ANDROID = RUMApplicationPlatformType("android")
RUMApplicationPlatformType.REACT_NATIVE = RUMApplicationPlatformType("react-native")
RUMApplicationPlatformType.FLUTTER = RUMApplicationPlatformType("flutter")
RUMApplicationPlatformType.ROKU = RUMApplicationPlatformType("roku")
RUMApplicationPlatformType.ELECTRON = RUMApplicationPlatformType("electron")
RUMApplicationPlatformType.UNITY = RUMApplicationPlatformType("unity")
RUMApplicationPlatformType.KOTLIN_MULTIPLATFORM = RUMApplicationPlatformType("kotlin-multiplatform")
RUMApplicationPlatformType.REACT = RUMApplicationPlatformType("react")
RUMApplicationPlatformType.NEXTJS = RUMApplicationPlatformType("nextjs")
RUMApplicationPlatformType.ANGULAR = RUMApplicationPlatformType("angular")
RUMApplicationPlatformType.VUEJS = RUMApplicationPlatformType("vuejs")
RUMApplicationPlatformType.NUXT = RUMApplicationPlatformType("nuxt")
RUMApplicationPlatformType.TANSTACK = RUMApplicationPlatformType("tanstack")
RUMApplicationPlatformType.MAUI = RUMApplicationPlatformType("maui")
RUMApplicationPlatformType.SALESFORCE_LWC = RUMApplicationPlatformType("salesforce-lwc")
RUMApplicationPlatformType.SHOPIFY = RUMApplicationPlatformType("shopify")
RUMApplicationPlatformType.CPP = RUMApplicationPlatformType("cpp")
RUMApplicationPlatformType.UNREAL = RUMApplicationPlatformType("unreal")
