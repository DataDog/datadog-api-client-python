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
    from datadog_api_client.v2.model.rum_segment_update_attributes import RumSegmentUpdateAttributes
    from datadog_api_client.v2.model.rum_segment_resource_type import RumSegmentResourceType


class RumSegmentUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_update_attributes import RumSegmentUpdateAttributes
        from datadog_api_client.v2.model.rum_segment_resource_type import RumSegmentResourceType

        return {
            "attributes": (RumSegmentUpdateAttributes,),
            "id": (str,),
            "type": (RumSegmentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumSegmentUpdateAttributes, id: str, type: RumSegmentResourceType, **kwargs):
        """
        Data object for a segment update request.

        :param attributes: Attributes for updating a segment. All fields are optional.
        :type attributes: RumSegmentUpdateAttributes

        :param id: The identifier of the segment to update.
        :type id: str

        :param type: Type of the segment resource.
        :type type: RumSegmentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
