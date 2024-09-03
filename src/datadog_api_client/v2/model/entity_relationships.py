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
    from datadog_api_client.v2.model.entity_to_incidents import EntityToIncidents
    from datadog_api_client.v2.model.entity_to_oncalls import EntityToOncalls
    from datadog_api_client.v2.model.entity_to_raw_schema import EntityToRawSchema
    from datadog_api_client.v2.model.entity_to_related_entities import EntityToRelatedEntities
    from datadog_api_client.v2.model.entity_to_schema import EntityToSchema


class EntityRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_to_incidents import EntityToIncidents
        from datadog_api_client.v2.model.entity_to_oncalls import EntityToOncalls
        from datadog_api_client.v2.model.entity_to_raw_schema import EntityToRawSchema
        from datadog_api_client.v2.model.entity_to_related_entities import EntityToRelatedEntities
        from datadog_api_client.v2.model.entity_to_schema import EntityToSchema

        return {
            "incidents": (EntityToIncidents,),
            "oncall": (EntityToOncalls,),
            "raw_schema": (EntityToRawSchema,),
            "related_entities": (EntityToRelatedEntities,),
            "schema": (EntityToSchema,),
        }

    attribute_map = {
        "incidents": "incidents",
        "oncall": "oncall",
        "raw_schema": "rawSchema",
        "related_entities": "relatedEntities",
        "schema": "schema",
    }

    def __init__(
        self_,
        incidents: Union[EntityToIncidents, UnsetType] = unset,
        oncall: Union[EntityToOncalls, UnsetType] = unset,
        raw_schema: Union[EntityToRawSchema, UnsetType] = unset,
        related_entities: Union[EntityToRelatedEntities, UnsetType] = unset,
        schema: Union[EntityToSchema, UnsetType] = unset,
        **kwargs,
    ):
        """
        Entity relationships.

        :param incidents: Entity to incidents relationship.
        :type incidents: EntityToIncidents, optional

        :param oncall: Entity to oncalls relationship.
        :type oncall: EntityToOncalls, optional

        :param raw_schema: Entity to raw schema relationship.
        :type raw_schema: EntityToRawSchema, optional

        :param related_entities: Entity to related entities relationship.
        :type related_entities: EntityToRelatedEntities, optional

        :param schema: Entity to detail schema relationship.
        :type schema: EntityToSchema, optional
        """
        if incidents is not unset:
            kwargs["incidents"] = incidents
        if oncall is not unset:
            kwargs["oncall"] = oncall
        if raw_schema is not unset:
            kwargs["raw_schema"] = raw_schema
        if related_entities is not unset:
            kwargs["related_entities"] = related_entities
        if schema is not unset:
            kwargs["schema"] = schema
        super().__init__(kwargs)
