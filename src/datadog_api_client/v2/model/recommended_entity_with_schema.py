# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_v3 import EntityV3
    from datadog_api_client.v2.model.entity_v3_service import EntityV3Service
    from datadog_api_client.v2.model.entity_v3_datastore import EntityV3Datastore
    from datadog_api_client.v2.model.entity_v3_queue import EntityV3Queue
    from datadog_api_client.v2.model.entity_v3_system import EntityV3System
    from datadog_api_client.v2.model.entity_v3_api import EntityV3API


class RecommendedEntityWithSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3 import EntityV3

        return {
            "id": (str,),
            "schema": (EntityV3,),
        }

    attribute_map = {
        "id": "id",
        "schema": "schema",
    }

    def __init__(
        self_,
        id: str,
        schema: Union[EntityV3, EntityV3Service, EntityV3Datastore, EntityV3Queue, EntityV3System, EntityV3API],
        **kwargs,
    ):
        """
        A recommended entity with its schema definition.

        :param id: Unique identifier for the recommended entity.
        :type id: str

        :param schema: Entity schema v3.
        :type schema: EntityV3
        """
        super().__init__(kwargs)

        self_.id = id
        self_.schema = schema
