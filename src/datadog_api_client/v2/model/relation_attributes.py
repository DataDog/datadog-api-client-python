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
    from datadog_api_client.v2.model.relation_entity import RelationEntity
    from datadog_api_client.v2.model.relation_type import RelationType


class RelationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relation_entity import RelationEntity
        from datadog_api_client.v2.model.relation_type import RelationType

        return {
            "_from": (RelationEntity,),
            "to": (RelationEntity,),
            "type": (RelationType,),
        }

    attribute_map = {
        "_from": "from",
        "to": "to",
        "type": "type",
    }

    def __init__(
        self_,
        _from: Union[RelationEntity, UnsetType] = unset,
        to: Union[RelationEntity, UnsetType] = unset,
        type: Union[RelationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relation attributes.

        :param _from: Relation entity reference.
        :type _from: RelationEntity, optional

        :param to: Relation entity reference.
        :type to: RelationEntity, optional

        :param type: Supported relation types.
        :type type: RelationType, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if to is not unset:
            kwargs["to"] = to
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
