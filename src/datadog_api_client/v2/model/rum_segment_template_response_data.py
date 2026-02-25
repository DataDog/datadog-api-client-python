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
    from datadog_api_client.v2.model.rum_segment_template_response_attributes import (
        RumSegmentTemplateResponseAttributes,
    )
    from datadog_api_client.v2.model.rum_segment_template_resource_type import RumSegmentTemplateResourceType


class RumSegmentTemplateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_template_response_attributes import (
            RumSegmentTemplateResponseAttributes,
        )
        from datadog_api_client.v2.model.rum_segment_template_resource_type import RumSegmentTemplateResourceType

        return {
            "attributes": (RumSegmentTemplateResponseAttributes,),
            "id": (str,),
            "type": (RumSegmentTemplateResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RumSegmentTemplateResponseAttributes, id: str, type: RumSegmentTemplateResourceType, **kwargs
    ):
        """
        Data object for a segment template in a response.

        :param attributes: Attributes of a segment template in a response.
        :type attributes: RumSegmentTemplateResponseAttributes

        :param id: The unique identifier of the template.
        :type id: str

        :param type: Type of the segment template resource.
        :type type: RumSegmentTemplateResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
