# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsApiMultistepSubtestType(ModelSimple):
    """
    Type of the subtest resource.

    :param value: If omitted defaults to "subtest". Must be one of ["subtest"].
    :type value: str
    """

    allowed_values = {
        "subtest",
    }
    SUBTEST: ClassVar["SyntheticsApiMultistepSubtestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsApiMultistepSubtestType.SUBTEST = SyntheticsApiMultistepSubtestType("subtest")
