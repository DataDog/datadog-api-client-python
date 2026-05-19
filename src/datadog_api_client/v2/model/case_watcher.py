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
    from datadog_api_client.v2.model.case_watcher_relationships import CaseWatcherRelationships
    from datadog_api_client.v2.model.case_watcher_resource_type import CaseWatcherResourceType


class CaseWatcher(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_watcher_relationships import CaseWatcherRelationships
        from datadog_api_client.v2.model.case_watcher_resource_type import CaseWatcherResourceType

        return {
            "id": (str,),
            "relationships": (CaseWatcherRelationships,),
            "type": (CaseWatcherResourceType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self_, id: str, relationships: CaseWatcherRelationships, type: CaseWatcherResourceType, **kwargs):
        """
        Represents a user who is subscribed to notifications for a case. Watchers receive updates when the case's status, priority, assignee, or comments change.

        :param id: The primary identifier of the case watcher.
        :type id: str

        :param relationships: Relationships for a case watcher, linking to the underlying user resource.
        :type relationships: CaseWatcherRelationships

        :param type: JSON:API resource type for case watchers.
        :type type: CaseWatcherResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.relationships = relationships
        self_.type = type
