# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmUnifiedHostFacetType(ModelSimple):
    """
    The JSON:API type for unified host facet resources. The value should always be `unified_host_facet`.

    :param value: If omitted defaults to "unified_host_facet". Must be one of ["unified_host_facet"].
    :type value: str
    """

    allowed_values = {
        "unified_host_facet",
    }
    UNIFIED_HOST_FACET: ClassVar["CsmUnifiedHostFacetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmUnifiedHostFacetType.UNIFIED_HOST_FACET = CsmUnifiedHostFacetType("unified_host_facet")
