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
    from datadog_api_client.v2.model.segment_attributes import SegmentAttributes
    from datadog_api_client.v2.model.segment_resource_type import SegmentResourceType


class SegmentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_attributes import SegmentAttributes
        from datadog_api_client.v2.model.segment_resource_type import SegmentResourceType

        return {
            "attributes": (SegmentAttributes,),
            "id": (str,),
            "type": (SegmentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SegmentAttributes, id: str, type: SegmentResourceType, **kwargs):
        """
        A segment.

        :param attributes: Attributes of a segment.
        :type attributes: SegmentAttributes

        :param id: ID of the segment.
        :type id: str

        :param type: Segment resource type.
        :type type: SegmentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
