# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumSegmentDeleteType(ModelSimple):
    """
    Type of the deleted segment resource.

    :param value: If omitted defaults to "deleted_segment". Must be one of ["deleted_segment"].
    :type value: str
    """

    allowed_values = {
        "deleted_segment",
    }
    DELETED_SEGMENT: ClassVar["RumSegmentDeleteType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumSegmentDeleteType.DELETED_SEGMENT = RumSegmentDeleteType("deleted_segment")
