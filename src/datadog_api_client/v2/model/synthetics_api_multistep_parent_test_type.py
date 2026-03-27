# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsApiMultistepParentTestType(ModelSimple):
    """
    Type of the parent test resource.

    :param value: If omitted defaults to "parent_test". Must be one of ["parent_test"].
    :type value: str
    """

    allowed_values = {
        "parent_test",
    }
    PARENT_TEST: ClassVar["SyntheticsApiMultistepParentTestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsApiMultistepParentTestType.PARENT_TEST = SyntheticsApiMultistepParentTestType("parent_test")
