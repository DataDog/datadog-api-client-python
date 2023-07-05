# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SpansListRequestType(ModelSimple):
    """
    The type of resource. The value should always be search_request.

    :param value: If omitted defaults to "search_request". Must be one of ["search_request"].
    :type value: str
    """

    allowed_values = {
        "search_request",
    }
    SEARCH_REQUEST: ClassVar["SpansListRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SpansListRequestType.SEARCH_REQUEST = SpansListRequestType("search_request")
