# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmFacetInfoType(ModelSimple):
    """
    The JSON:API type for facet info resources. The value should always be `facet_info`.

    :param value: If omitted defaults to "facet_info". Must be one of ["facet_info"].
    :type value: str
    """

    allowed_values = {
        "facet_info",
    }
    FACET_INFO: ClassVar["CsmFacetInfoType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmFacetInfoType.FACET_INFO = CsmFacetInfoType("facet_info")
