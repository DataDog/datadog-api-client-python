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
    from datadog_api_client.v2.model.entity_attributes import EntityAttributes
    from datadog_api_client.v2.model.entity_meta import EntityMeta
    from datadog_api_client.v2.model.entity_relationships import EntityRelationships


class EntityData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_attributes import EntityAttributes
        from datadog_api_client.v2.model.entity_meta import EntityMeta
        from datadog_api_client.v2.model.entity_relationships import EntityRelationships

        return {
            "attributes": (EntityAttributes,),
            "id": (str,),
            "meta": (EntityMeta,),
            "relationships": (EntityRelationships,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[EntityAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[EntityMeta, UnsetType] = unset,
        relationships: Union[EntityRelationships, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Entity data.

        :param attributes: Entity attributes.
        :type attributes: EntityAttributes, optional

        :param id: Entity id.
        :type id: str, optional

        :param meta: Entity metadata.
        :type meta: EntityMeta, optional

        :param relationships: Entity relationships.
        :type relationships: EntityRelationships, optional

        :param type: Entity.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
