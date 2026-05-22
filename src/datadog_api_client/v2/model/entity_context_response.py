# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_context_entity import EntityContextEntity
    from datadog_api_client.v2.model.entity_context_response_meta import EntityContextResponseMeta


class EntityContextResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_entity import EntityContextEntity
        from datadog_api_client.v2.model.entity_context_response_meta import EntityContextResponseMeta

        return {
            "data": ([EntityContextEntity],),
            "meta": (EntityContextResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[EntityContextEntity], meta: EntityContextResponseMeta, **kwargs):
        """
        Response from the entity context endpoint, containing the matching entities and pagination metadata.

        :param data: The list of entities matching the query.
        :type data: [EntityContextEntity]

        :param meta: Metadata returned alongside the entity context response.
        :type meta: EntityContextResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
