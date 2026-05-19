# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomAttributeType(ModelSimple):
    """
    Custom attributes type

    :param value: Must be one of ["URL", "TEXT", "NUMBER", "SELECT"].
    :type value: str
    """

    allowed_values = {
        "URL",
        "TEXT",
        "NUMBER",
        "SELECT",
    }
    URL: ClassVar["CustomAttributeType"]
    TEXT: ClassVar["CustomAttributeType"]
    NUMBER: ClassVar["CustomAttributeType"]
    SELECT: ClassVar["CustomAttributeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomAttributeType.URL = CustomAttributeType("URL")
CustomAttributeType.TEXT = CustomAttributeType("TEXT")
CustomAttributeType.NUMBER = CustomAttributeType("NUMBER")
CustomAttributeType.SELECT = CustomAttributeType("SELECT")
