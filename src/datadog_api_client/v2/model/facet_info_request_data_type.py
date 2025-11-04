# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FacetInfoRequestDataType(ModelSimple):
    """
    Users facet info request resource type.

    :param value: If omitted defaults to "users_facet_info_request". Must be one of ["users_facet_info_request"].
    :type value: str
    """

    allowed_values = {
        "users_facet_info_request",
    }
    USERS_FACET_INFO_REQUEST: ClassVar["FacetInfoRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FacetInfoRequestDataType.USERS_FACET_INFO_REQUEST = FacetInfoRequestDataType("users_facet_info_request")
