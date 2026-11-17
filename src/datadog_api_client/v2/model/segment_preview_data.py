# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.segment_preview_attributes import SegmentPreviewAttributes
    from datadog_api_client.v2.model.segment_preview_request_type import SegmentPreviewRequestType


class SegmentPreviewData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_preview_attributes import SegmentPreviewAttributes
        from datadog_api_client.v2.model.segment_preview_request_type import SegmentPreviewRequestType

        return {
            "attributes": (SegmentPreviewAttributes,),
            "type": (SegmentPreviewRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: SegmentPreviewAttributes, type: SegmentPreviewRequestType, **kwargs):
        """
        Data of the segment preview request.

        :param attributes: Segment definition to preview and the columns to return.
            Without columns, the response returns the user ID, or the account ID for account segments.
        :type attributes: SegmentPreviewAttributes

        :param type: Segment preview request resource type.
        :type type: SegmentPreviewRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
