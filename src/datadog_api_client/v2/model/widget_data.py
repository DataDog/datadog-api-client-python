# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.widget_attributes import WidgetAttributes
    from datadog_api_client.v2.model.widget_relationships import WidgetRelationships


class WidgetData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_attributes import WidgetAttributes
        from datadog_api_client.v2.model.widget_relationships import WidgetRelationships

        return {
            "attributes": (WidgetAttributes,),
            "id": (str,),
            "relationships": (WidgetRelationships,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: WidgetAttributes,
        id: str,
        type: str,
        relationships: Union[WidgetRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A widget resource object.

        :param attributes: Attributes of a widget resource.
        :type attributes: WidgetAttributes

        :param id: The unique identifier of the widget.
        :type id: str

        :param relationships: Relationships of the widget resource.
        :type relationships: WidgetRelationships, optional

        :param type: Widgets resource type.
        :type type: str
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
