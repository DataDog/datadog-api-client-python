# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumStaticSegmentRequestType(ModelSimple):
    """
    Type of the static segment creation request resource.

    :param value: If omitted defaults to "create_static_segment_request". Must be one of ["create_static_segment_request"].
    :type value: str
    """

    allowed_values = {
        "create_static_segment_request",
    }
    CREATE_STATIC_SEGMENT_REQUEST: ClassVar["RumStaticSegmentRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumStaticSegmentRequestType.CREATE_STATIC_SEGMENT_REQUEST = RumStaticSegmentRequestType("create_static_segment_request")
