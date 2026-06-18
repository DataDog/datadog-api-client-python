# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumSdkConfigMatchOptionSerializedType(ModelSimple):
    """
    The type of match pattern, either a literal string or a regex.

    :param value: Must be one of ["string", "regex"].
    :type value: str
    """

    allowed_values = {
        "string",
        "regex",
    }
    STRING: ClassVar["RumSdkConfigMatchOptionSerializedType"]
    REGEX: ClassVar["RumSdkConfigMatchOptionSerializedType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumSdkConfigMatchOptionSerializedType.STRING = RumSdkConfigMatchOptionSerializedType("string")
RumSdkConfigMatchOptionSerializedType.REGEX = RumSdkConfigMatchOptionSerializedType("regex")
