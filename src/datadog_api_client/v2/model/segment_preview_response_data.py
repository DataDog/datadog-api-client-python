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
    from datadog_api_client.v2.model.segment_preview_response_attributes import SegmentPreviewResponseAttributes
    from datadog_api_client.v2.model.segment_preview_response_type import SegmentPreviewResponseType


class SegmentPreviewResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_preview_response_attributes import SegmentPreviewResponseAttributes
        from datadog_api_client.v2.model.segment_preview_response_type import SegmentPreviewResponseType

        return {
            "attributes": (SegmentPreviewResponseAttributes,),
            "id": (str,),
            "type": (SegmentPreviewResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SegmentPreviewResponseAttributes, id: str, type: SegmentPreviewResponseType, **kwargs
    ):
        """
        Data of the segment preview response.

        :param attributes: Members of the previewed segment.
        :type attributes: SegmentPreviewResponseAttributes

        :param id: ID of the preview response.
        :type id: str

        :param type: Segment preview response resource type.
        :type type: SegmentPreviewResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
