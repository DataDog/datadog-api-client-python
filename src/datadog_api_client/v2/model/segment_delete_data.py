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
    from datadog_api_client.v2.model.segment_delete_attributes import SegmentDeleteAttributes
    from datadog_api_client.v2.model.segment_deleted_type import SegmentDeletedType


class SegmentDeleteData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_delete_attributes import SegmentDeleteAttributes
        from datadog_api_client.v2.model.segment_deleted_type import SegmentDeletedType

        return {
            "attributes": (SegmentDeleteAttributes,),
            "id": (str,),
            "type": (SegmentDeletedType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SegmentDeleteAttributes, id: str, type: SegmentDeletedType, **kwargs):
        """
        A deleted segment.

        :param attributes: Attributes of a deleted segment.
        :type attributes: SegmentDeleteAttributes

        :param id: ID of the segment.
        :type id: str

        :param type: Deleted segment resource type.
        :type type: SegmentDeletedType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
