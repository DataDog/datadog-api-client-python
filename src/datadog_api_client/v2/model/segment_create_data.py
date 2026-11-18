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
    from datadog_api_client.v2.model.segment_create_attributes import SegmentCreateAttributes
    from datadog_api_client.v2.model.segment_resource_type import SegmentResourceType


class SegmentCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_create_attributes import SegmentCreateAttributes
        from datadog_api_client.v2.model.segment_resource_type import SegmentResourceType

        return {
            "attributes": (SegmentCreateAttributes,),
            "type": (SegmentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: SegmentCreateAttributes, type: SegmentResourceType, **kwargs):
        """
        Data of the segment to create.

        :param attributes: Attributes of the segment to create.
        :type attributes: SegmentCreateAttributes

        :param type: Segment resource type.
        :type type: SegmentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
