# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SegmentPreviewResponseType(ModelSimple):
    """
    Segment preview response resource type.

    :param value: If omitted defaults to "unified_segment_preview_response". Must be one of ["unified_segment_preview_response"].
    :type value: str
    """

    allowed_values = {
        "unified_segment_preview_response",
    }
    UNIFIED_SEGMENT_PREVIEW_RESPONSE: ClassVar["SegmentPreviewResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SegmentPreviewResponseType.UNIFIED_SEGMENT_PREVIEW_RESPONSE = SegmentPreviewResponseType(
    "unified_segment_preview_response"
)
