# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TableResultV2DataType(ModelSimple):
    """
    Reference table resource type.

    :param value: If omitted defaults to "reference_table". Must be one of ["reference_table"].
    :type value: str
    """

    allowed_values = {
        "reference_table",
    }
    REFERENCE_TABLE: ClassVar["TableResultV2DataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TableResultV2DataType.REFERENCE_TABLE = TableResultV2DataType("reference_table")
