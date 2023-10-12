# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceDefinitionV2Dot2Type(ModelSimple):
    """
    The type of service.

    :param value: Must be one of ["web", "db", "cache", "function", "browser", "mobile", "custom"].
    :type value: str
    """

    allowed_values = {
        "web",
        "db",
        "cache",
        "function",
        "browser",
        "mobile",
        "custom",
    }
    WEB: ClassVar["ServiceDefinitionV2Dot2Type"]
    DB: ClassVar["ServiceDefinitionV2Dot2Type"]
    CACHE: ClassVar["ServiceDefinitionV2Dot2Type"]
    FUNCTION: ClassVar["ServiceDefinitionV2Dot2Type"]
    BROSWER: ClassVar["ServiceDefinitionV2Dot2Type"]
    MOBILE: ClassVar["ServiceDefinitionV2Dot2Type"]
    CUSTOM: ClassVar["ServiceDefinitionV2Dot2Type"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceDefinitionV2Dot2Type.WEB = ServiceDefinitionV2Dot2Type("web")
ServiceDefinitionV2Dot2Type.DB = ServiceDefinitionV2Dot2Type("db")
ServiceDefinitionV2Dot2Type.CACHE = ServiceDefinitionV2Dot2Type("cache")
ServiceDefinitionV2Dot2Type.FUNCTION = ServiceDefinitionV2Dot2Type("function")
ServiceDefinitionV2Dot2Type.BROSWER = ServiceDefinitionV2Dot2Type("browser")
ServiceDefinitionV2Dot2Type.MOBILE = ServiceDefinitionV2Dot2Type("mobile")
ServiceDefinitionV2Dot2Type.CUSTOM = ServiceDefinitionV2Dot2Type("custom")
