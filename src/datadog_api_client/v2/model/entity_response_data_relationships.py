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
    from datadog_api_client.v2.model.entity_response_data_relationships_incidents import (
        EntityResponseDataRelationshipsIncidents,
    )
    from datadog_api_client.v2.model.entity_response_data_relationships_oncalls import (
        EntityResponseDataRelationshipsOncalls,
    )
    from datadog_api_client.v2.model.entity_response_data_relationships_raw_schema import (
        EntityResponseDataRelationshipsRawSchema,
    )
    from datadog_api_client.v2.model.entity_response_data_relationships_related_entities import (
        EntityResponseDataRelationshipsRelatedEntities,
    )
    from datadog_api_client.v2.model.entity_response_data_relationships_schema import (
        EntityResponseDataRelationshipsSchema,
    )


class EntityResponseDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_data_relationships_incidents import (
            EntityResponseDataRelationshipsIncidents,
        )
        from datadog_api_client.v2.model.entity_response_data_relationships_oncalls import (
            EntityResponseDataRelationshipsOncalls,
        )
        from datadog_api_client.v2.model.entity_response_data_relationships_raw_schema import (
            EntityResponseDataRelationshipsRawSchema,
        )
        from datadog_api_client.v2.model.entity_response_data_relationships_related_entities import (
            EntityResponseDataRelationshipsRelatedEntities,
        )
        from datadog_api_client.v2.model.entity_response_data_relationships_schema import (
            EntityResponseDataRelationshipsSchema,
        )

        return {
            "incidents": (EntityResponseDataRelationshipsIncidents,),
            "oncalls": (EntityResponseDataRelationshipsOncalls,),
            "raw_schema": (EntityResponseDataRelationshipsRawSchema,),
            "related_entities": (EntityResponseDataRelationshipsRelatedEntities,),
            "schema": (EntityResponseDataRelationshipsSchema,),
        }

    attribute_map = {
        "incidents": "incidents",
        "oncalls": "oncalls",
        "raw_schema": "rawSchema",
        "related_entities": "relatedEntities",
        "schema": "schema",
    }

    def __init__(
        self_,
        incidents: Union[EntityResponseDataRelationshipsIncidents, UnsetType] = unset,
        oncalls: Union[EntityResponseDataRelationshipsOncalls, UnsetType] = unset,
        raw_schema: Union[EntityResponseDataRelationshipsRawSchema, UnsetType] = unset,
        related_entities: Union[EntityResponseDataRelationshipsRelatedEntities, UnsetType] = unset,
        schema: Union[EntityResponseDataRelationshipsSchema, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param incidents:
        :type incidents: EntityResponseDataRelationshipsIncidents, optional

        :param oncalls:
        :type oncalls: EntityResponseDataRelationshipsOncalls, optional

        :param raw_schema:
        :type raw_schema: EntityResponseDataRelationshipsRawSchema, optional

        :param related_entities:
        :type related_entities: EntityResponseDataRelationshipsRelatedEntities, optional

        :param schema:
        :type schema: EntityResponseDataRelationshipsSchema, optional
        """
        if incidents is not unset:
            kwargs["incidents"] = incidents
        if oncalls is not unset:
            kwargs["oncalls"] = oncalls
        if raw_schema is not unset:
            kwargs["raw_schema"] = raw_schema
        if related_entities is not unset:
            kwargs["related_entities"] = related_entities
        if schema is not unset:
            kwargs["schema"] = schema
        super().__init__(kwargs)
