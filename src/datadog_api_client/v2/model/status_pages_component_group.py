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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.status_pages_component_group_attributes import StatusPagesComponentGroupAttributes
    from datadog_api_client.v2.model.status_pages_component_group_relationships import (
        StatusPagesComponentGroupRelationships,
    )
    from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType


class StatusPagesComponentGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_group_attributes import (
            StatusPagesComponentGroupAttributes,
        )
        from datadog_api_client.v2.model.status_pages_component_group_relationships import (
            StatusPagesComponentGroupRelationships,
        )
        from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

        return {
            "attributes": (StatusPagesComponentGroupAttributes,),
            "id": (UUID,),
            "relationships": (StatusPagesComponentGroupRelationships,),
            "type": (StatusPagesComponentGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: StatusPagesComponentGroupType,
        attributes: Union[StatusPagesComponentGroupAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        relationships: Union[StatusPagesComponentGroupRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The included component group resource.

        :param attributes: The attributes of a component group.
        :type attributes: StatusPagesComponentGroupAttributes, optional

        :param id: The ID of the component.
        :type id: UUID, optional

        :param relationships: The relationships of a component group.
        :type relationships: StatusPagesComponentGroupRelationships, optional

        :param type: Components resource type.
        :type type: StatusPagesComponentGroupType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
