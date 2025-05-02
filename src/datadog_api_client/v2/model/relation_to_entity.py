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
    from datadog_api_client.v2.model.relationship_item import RelationshipItem
    from datadog_api_client.v2.model.entity_meta import EntityMeta


class RelationToEntity(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_item import RelationshipItem
        from datadog_api_client.v2.model.entity_meta import EntityMeta

        return {
            "data": (RelationshipItem,),
            "meta": (EntityMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: Union[RelationshipItem, UnsetType] = unset, meta: Union[EntityMeta, UnsetType] = unset, **kwargs
    ):
        """
        Relation to entity.

        :param data: Relationship entry.
        :type data: RelationshipItem, optional

        :param meta: Entity metadata.
        :type meta: EntityMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
