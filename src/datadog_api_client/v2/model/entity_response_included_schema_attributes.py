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
    from datadog_api_client.v2.model.entity_v3 import EntityV3
    from datadog_api_client.v2.model.entity_v3_service import EntityV3Service
    from datadog_api_client.v2.model.entity_v3_datastore import EntityV3Datastore
    from datadog_api_client.v2.model.entity_v3_queue import EntityV3Queue
    from datadog_api_client.v2.model.entity_v3_system import EntityV3System


class EntityResponseIncludedSchemaAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3 import EntityV3

        return {
            "schema": (EntityV3,),
        }

    attribute_map = {
        "schema": "schema",
    }

    def __init__(
        self_,
        schema: Union[EntityV3, EntityV3Service, EntityV3Datastore, EntityV3Queue, EntityV3System, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included schema.

        :param schema: Entity schema v3.
        :type schema: EntityV3, optional
        """
        if schema is not unset:
            kwargs["schema"] = schema
        super().__init__(kwargs)
