# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppProtectionLevelType(ModelSimple):
    """
    The protection-level resource type.

    :param value: If omitted defaults to "protectionLevel". Must be one of ["protectionLevel"].
    :type value: str
    """

    allowed_values = {
        "protectionLevel",
    }
    PROTECTIONLEVEL: ClassVar["AppProtectionLevelType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppProtectionLevelType.PROTECTIONLEVEL = AppProtectionLevelType("protectionLevel")
