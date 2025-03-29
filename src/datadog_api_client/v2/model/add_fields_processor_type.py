# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AddFieldsProcessorType(ModelSimple):
    """
    The definition of `AddFieldsProcessorType` object.

    :param value: If omitted defaults to "add_fields". Must be one of ["add_fields"].
    :type value: str
    """

    allowed_values = {
        "add_fields",
    }
    ADD_FIELDS: ClassVar["AddFieldsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AddFieldsProcessorType.ADD_FIELDS = AddFieldsProcessorType("add_fields")
