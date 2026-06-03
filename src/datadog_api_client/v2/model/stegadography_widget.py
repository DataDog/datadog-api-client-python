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
    from datadog_api_client.v2.model.stegadography_widget_attributes import StegadographyWidgetAttributes
    from datadog_api_client.v2.model.stegadography_widget_type import StegadographyWidgetType


class StegadographyWidget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stegadography_widget_attributes import StegadographyWidgetAttributes
        from datadog_api_client.v2.model.stegadography_widget_type import StegadographyWidgetType

        return {
            "attributes": (StegadographyWidgetAttributes,),
            "id": (str,),
            "type": (StegadographyWidgetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: StegadographyWidgetAttributes, id: str, type: StegadographyWidgetType, **kwargs):
        """
        A single watermarked widget resource recovered from an image.

        :param attributes: Attributes of a watermarked widget recovered from an image.
        :type attributes: StegadographyWidgetAttributes

        :param id: Composite identifier formed from the organization ID and watermark, separated by a colon.
        :type id: str

        :param type: Stegadography widget resource type.
        :type type: StegadographyWidgetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
