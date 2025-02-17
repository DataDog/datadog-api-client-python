# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ColumnOrderObjectType(ModelSimple):
    """
    type of column

    :param value: Must be one of ["formula", "group"].
    :type value: str
    """

    allowed_values = {
        "formula",
        "group",
    }
    FORMULA: ClassVar["ColumnOrderObjectType"]
    GROUP: ClassVar["ColumnOrderObjectType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ColumnOrderObjectType.FORMULA = ColumnOrderObjectType("formula")
ColumnOrderObjectType.GROUP = ColumnOrderObjectType("group")
