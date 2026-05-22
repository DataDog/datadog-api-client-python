# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_context_entity_attributes import EntityContextEntityAttributes


class EntityContextEntity(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_entity_attributes import EntityContextEntityAttributes

        return {
            "attributes": (EntityContextEntityAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: EntityContextEntityAttributes, id: str, **kwargs):
        """
        A single entity returned by the entity context endpoint.

        :param attributes: The attributes of an entity context entry, grouping all the historical revisions of the entity.
        :type attributes: EntityContextEntityAttributes

        :param id: The unique identifier of the entity.
        :type id: str

        :param type: The type of the entity. Reflects the underlying entity kind from the entity context store
            (for example, ``siem_entity_identity`` for identities). Defaults to ``entity`` when the kind is unknown.
        :type type: str
        """
        super().__init__(kwargs)
        type = kwargs.get("type", "entity")

        self_.attributes = attributes
        self_.id = id
        self_.type = type
