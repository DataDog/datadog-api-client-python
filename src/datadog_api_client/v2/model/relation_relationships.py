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
    from datadog_api_client.v2.model.relation_to_entity import RelationToEntity


class RelationRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relation_to_entity import RelationToEntity

        return {
            "from_entity": (RelationToEntity,),
            "to_entity": (RelationToEntity,),
        }

    attribute_map = {
        "from_entity": "fromEntity",
        "to_entity": "toEntity",
    }

    def __init__(
        self_,
        from_entity: Union[RelationToEntity, UnsetType] = unset,
        to_entity: Union[RelationToEntity, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relation relationships.

        :param from_entity: Relation to entity.
        :type from_entity: RelationToEntity, optional

        :param to_entity: Relation to entity.
        :type to_entity: RelationToEntity, optional
        """
        if from_entity is not unset:
            kwargs["from_entity"] = from_entity
        if to_entity is not unset:
            kwargs["to_entity"] = to_entity
        super().__init__(kwargs)
