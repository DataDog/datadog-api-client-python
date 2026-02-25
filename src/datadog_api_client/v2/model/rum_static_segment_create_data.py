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
    from datadog_api_client.v2.model.rum_static_segment_create_attributes import RumStaticSegmentCreateAttributes
    from datadog_api_client.v2.model.rum_static_segment_request_type import RumStaticSegmentRequestType


class RumStaticSegmentCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_static_segment_create_attributes import RumStaticSegmentCreateAttributes
        from datadog_api_client.v2.model.rum_static_segment_request_type import RumStaticSegmentRequestType

        return {
            "attributes": (RumStaticSegmentCreateAttributes,),
            "type": (RumStaticSegmentRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RumStaticSegmentCreateAttributes, type: RumStaticSegmentRequestType, **kwargs):
        """
        Data object for a static segment creation request.

        :param attributes: Attributes for creating a new static segment.
        :type attributes: RumStaticSegmentCreateAttributes

        :param type: Type of the static segment creation request resource.
        :type type: RumStaticSegmentRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
