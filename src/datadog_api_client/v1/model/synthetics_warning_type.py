# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsWarningType(ModelSimple):
    """
    User locator used.

    :param value: If omitted defaults to "user_locator". Must be one of ["user_locator"].
    :type value: str
    """

    allowed_values = {
        "user_locator",
    }
    USER_LOCATOR: ClassVar["SyntheticsWarningType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsWarningType.USER_LOCATOR = SyntheticsWarningType("user_locator")
