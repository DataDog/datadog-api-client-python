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
    from datadog_api_client.v2.model.status_pages_component_data_attributes import StatusPagesComponentDataAttributes
    from datadog_api_client.v2.model.status_pages_component_data_relationships import (
        StatusPagesComponentDataRelationships,
    )
    from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType


class StatusPagesComponentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_data_attributes import (
            StatusPagesComponentDataAttributes,
        )
        from datadog_api_client.v2.model.status_pages_component_data_relationships import (
            StatusPagesComponentDataRelationships,
        )
        from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

        return {
            "attributes": (StatusPagesComponentDataAttributes,),
            "id": (UUID,),
            "relationships": (StatusPagesComponentDataRelationships,),
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
        attributes: Union[StatusPagesComponentDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        relationships: Union[StatusPagesComponentDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: The attributes of a component.
        :type attributes: StatusPagesComponentDataAttributes, optional

        :param id: The ID of the component.
        :type id: UUID, optional

        :param relationships: The relationships of a component.
        :type relationships: StatusPagesComponentDataRelationships, optional

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
