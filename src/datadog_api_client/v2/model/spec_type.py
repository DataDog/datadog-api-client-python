# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SpecType(ModelSimple):
    """
    Type of the spec resource.

    :param value: If omitted defaults to "spec". Must be one of ["spec"].
    :type value: str
    """

    allowed_values = {
        "spec",
    }
    SPEC: ClassVar["SpecType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SpecType.SPEC = SpecType("spec")
