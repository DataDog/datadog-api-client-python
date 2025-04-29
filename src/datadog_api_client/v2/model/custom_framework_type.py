# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomFrameworkType(ModelSimple):
    """
    The type of the resource. The value must be `custom_framework`.

    :param value: If omitted defaults to "custom_framework". Must be one of ["custom_framework"].
    :type value: str
    """

    allowed_values = {
        "custom_framework",
    }
    CUSTOM_FRAMEWORK: ClassVar["CustomFrameworkType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomFrameworkType.CUSTOM_FRAMEWORK = CustomFrameworkType("custom_framework")
