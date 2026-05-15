# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsScalarColumnType(ModelSimple):
    """
    The column type. "group" for dimension columns, "number" for metric columns.

    :param value: Must be one of ["group", "number"].
    :type value: str
    """

    allowed_values = {
        "group",
        "number",
    }
    GROUP: ClassVar["CommitmentsScalarColumnType"]
    NUMBER: ClassVar["CommitmentsScalarColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsScalarColumnType.GROUP = CommitmentsScalarColumnType("group")
CommitmentsScalarColumnType.NUMBER = CommitmentsScalarColumnType("number")
