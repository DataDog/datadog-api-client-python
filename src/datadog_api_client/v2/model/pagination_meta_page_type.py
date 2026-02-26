# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PaginationMetaPageType(ModelSimple):
    """


    :param value: If omitted defaults to "offset_limit". Must be one of ["offset_limit"].
    :type value: str
    """

    allowed_values = {
        "offset_limit",
    }
    OFFSET_LIMIT: ClassVar["PaginationMetaPageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PaginationMetaPageType.OFFSET_LIMIT = PaginationMetaPageType("offset_limit")
