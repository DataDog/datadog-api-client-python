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
    from datadog_api_client.v2.model.entity_response_data_relationships_incidents_data_items_type import (
        EntityResponseDataRelationshipsIncidentsDataItemsType,
    )


class EntityResponseDataRelationshipsIncidentsDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_data_relationships_incidents_data_items_type import (
            EntityResponseDataRelationshipsIncidentsDataItemsType,
        )

        return {
            "id": (str,),
            "type": (EntityResponseDataRelationshipsIncidentsDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: EntityResponseDataRelationshipsIncidentsDataItemsType, **kwargs):
        """


        :param id:
        :type id: str

        :param type: Incident resource type.
        :type type: EntityResponseDataRelationshipsIncidentsDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
