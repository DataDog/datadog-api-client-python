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
    from datadog_api_client.v2.model.rum_segment_delete_attributes import RumSegmentDeleteAttributes
    from datadog_api_client.v2.model.rum_segment_delete_type import RumSegmentDeleteType


class RumSegmentDeleteData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_delete_attributes import RumSegmentDeleteAttributes
        from datadog_api_client.v2.model.rum_segment_delete_type import RumSegmentDeleteType

        return {
            "attributes": (RumSegmentDeleteAttributes,),
            "id": (str,),
            "type": (RumSegmentDeleteType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumSegmentDeleteAttributes, id: str, type: RumSegmentDeleteType, **kwargs):
        """
        Data object for a deleted segment response.

        :param attributes: Attributes of a deleted segment response.
        :type attributes: RumSegmentDeleteAttributes

        :param id: Unique identifier for the deleted segment.
        :type id: str

        :param type: Type of the deleted segment resource.
        :type type: RumSegmentDeleteType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
