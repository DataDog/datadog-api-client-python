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
    from datadog_api_client.v2.model.watcher_relationships import WatcherRelationships
    from datadog_api_client.v2.model.watcher_resource_type import WatcherResourceType


class Watcher(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.watcher_relationships import WatcherRelationships
        from datadog_api_client.v2.model.watcher_resource_type import WatcherResourceType

        return {
            "id": (str,),
            "relationships": (WatcherRelationships,),
            "type": (WatcherResourceType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self_, id: str, relationships: WatcherRelationships, type: WatcherResourceType, **kwargs):
        """
        Case watcher

        :param id: User UUID of the watcher
        :type id: str

        :param relationships: Watcher relationships
        :type relationships: WatcherRelationships

        :param type: Watcher resource type
        :type type: WatcherResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.relationships = relationships
        self_.type = type
