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
    from datadog_api_client.v2.model.entity_response_included_related_entity_attributes import (
        EntityResponseIncludedRelatedEntityAttributes,
    )
    from datadog_api_client.v2.model.entity_response_included_related_entity_meta import (
        EntityResponseIncludedRelatedEntityMeta,
    )
    from datadog_api_client.v2.model.entity_response_included_related_entity_type import (
        EntityResponseIncludedRelatedEntityType,
    )


class EntityResponseIncludedRelatedEntity(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_included_related_entity_attributes import (
            EntityResponseIncludedRelatedEntityAttributes,
        )
        from datadog_api_client.v2.model.entity_response_included_related_entity_meta import (
            EntityResponseIncludedRelatedEntityMeta,
        )
        from datadog_api_client.v2.model.entity_response_included_related_entity_type import (
            EntityResponseIncludedRelatedEntityType,
        )

        return {
            "attributes": (EntityResponseIncludedRelatedEntityAttributes,),
            "id": (str,),
            "meta": (EntityResponseIncludedRelatedEntityMeta,),
            "type": (EntityResponseIncludedRelatedEntityType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[EntityResponseIncludedRelatedEntityAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[EntityResponseIncludedRelatedEntityMeta, UnsetType] = unset,
        type: Union[EntityResponseIncludedRelatedEntityType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included related entity.

        :param attributes: Related entity attributes.
        :type attributes: EntityResponseIncludedRelatedEntityAttributes, optional

        :param id: Entity UUID.
        :type id: str, optional

        :param meta: Included related entity meta.
        :type meta: EntityResponseIncludedRelatedEntityMeta, optional

        :param type: Related entity.
        :type type: EntityResponseIncludedRelatedEntityType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
