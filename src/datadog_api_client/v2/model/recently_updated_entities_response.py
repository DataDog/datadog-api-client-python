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


class RecentlyUpdatedEntitiesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_entity import EntityContextEntity

        return {
            "data": ([EntityContextEntity],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[EntityContextEntity], **kwargs):
        """
        Response from the recently updated entities endpoint, containing the entities with the most recent updates in the requested time range, ordered from most to least recently updated.

        :param data: The list of entities with the most recent updates, ordered from most to least recently updated.
        :type data: [EntityContextEntity]
        """
        super().__init__(kwargs)

        self_.data = data
