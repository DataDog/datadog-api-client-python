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
    from datadog_api_client.v2.model.widget_relationship_item import WidgetRelationshipItem


class WidgetRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_relationship_item import WidgetRelationshipItem

        return {
            "created_by": (WidgetRelationshipItem,),
            "modified_by": (WidgetRelationshipItem,),
        }

    attribute_map = {
        "created_by": "created_by",
        "modified_by": "modified_by",
    }

    def __init__(
        self_,
        created_by: Union[WidgetRelationshipItem, UnsetType] = unset,
        modified_by: Union[WidgetRelationshipItem, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of the widget resource.

        :param created_by: A JSON:API relationship to a user.
        :type created_by: WidgetRelationshipItem, optional

        :param modified_by: A JSON:API relationship to a user.
        :type modified_by: WidgetRelationshipItem, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        super().__init__(kwargs)
