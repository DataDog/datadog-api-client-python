# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormDataDefinitionType(ModelSimple):
    """
    The root schema type.

    :param value: If omitted defaults to "object". Must be one of ["object"].
    :type value: str
    """

    allowed_values = {
        "object",
    }
    OBJECT: ClassVar["FormDataDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormDataDefinitionType.OBJECT = FormDataDefinitionType("object")
