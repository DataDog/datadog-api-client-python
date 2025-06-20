# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeEventCustomAttributesAuthorType(ModelSimple):
    """
    Author's type.

    :param value: Must be one of ["user", "system", "api", "automation"].
    :type value: str
    """

    allowed_values = {
        "user",
        "system",
        "api",
        "automation",
    }
    USER: ClassVar["ChangeEventCustomAttributesAuthorType"]
    SYSTEM: ClassVar["ChangeEventCustomAttributesAuthorType"]
    API: ClassVar["ChangeEventCustomAttributesAuthorType"]
    AUTOMATION: ClassVar["ChangeEventCustomAttributesAuthorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeEventCustomAttributesAuthorType.USER = ChangeEventCustomAttributesAuthorType("user")
ChangeEventCustomAttributesAuthorType.SYSTEM = ChangeEventCustomAttributesAuthorType("system")
ChangeEventCustomAttributesAuthorType.API = ChangeEventCustomAttributesAuthorType("api")
ChangeEventCustomAttributesAuthorType.AUTOMATION = ChangeEventCustomAttributesAuthorType("automation")
