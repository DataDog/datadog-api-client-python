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
    from datadog_api_client.v2.model.relation_attributes import RelationAttributes
    from datadog_api_client.v2.model.relation_meta import RelationMeta
    from datadog_api_client.v2.model.relation_relationships import RelationRelationships
    from datadog_api_client.v2.model.relation_response_type import RelationResponseType


class RelationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relation_attributes import RelationAttributes
        from datadog_api_client.v2.model.relation_meta import RelationMeta
        from datadog_api_client.v2.model.relation_relationships import RelationRelationships
        from datadog_api_client.v2.model.relation_response_type import RelationResponseType

        return {
            "attributes": (RelationAttributes,),
            "id": (str,),
            "meta": (RelationMeta,),
            "relationships": (RelationRelationships,),
            "subtype": (str,),
            "type": (RelationResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "relationships": "relationships",
        "subtype": "subtype",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RelationAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[RelationMeta, UnsetType] = unset,
        relationships: Union[RelationRelationships, UnsetType] = unset,
        subtype: Union[str, UnsetType] = unset,
        type: Union[RelationResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relation response data.

        :param attributes: Relation attributes.
        :type attributes: RelationAttributes, optional

        :param id: Relation ID.
        :type id: str, optional

        :param meta: Relation metadata.
        :type meta: RelationMeta, optional

        :param relationships: Relation relationships.
        :type relationships: RelationRelationships, optional

        :param subtype: Relation subtype.
        :type subtype: str, optional

        :param type: Relation type.
        :type type: RelationResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if subtype is not unset:
            kwargs["subtype"] = subtype
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
