# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_context_revision_attributes import EntityContextRevisionAttributes


class EntityContextRevision(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_revision_attributes import EntityContextRevisionAttributes

        return {
            "attributes": (EntityContextRevisionAttributes,),
            "first_seen_at": (datetime,),
            "last_seen_at": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "first_seen_at": "first_seen_at",
        "last_seen_at": "last_seen_at",
    }

    def __init__(
        self_, attributes: EntityContextRevisionAttributes, first_seen_at: datetime, last_seen_at: datetime, **kwargs
    ):
        """
        A single historical revision of an entity, including the time range during which the revision was observed.

        :param attributes: The set of attributes recorded for the entity at this revision. The keys depend on the kind of entity.
        :type attributes: EntityContextRevisionAttributes

        :param first_seen_at: The first time the entity was observed at this revision.
        :type first_seen_at: datetime

        :param last_seen_at: The last time the entity was observed at this revision.
        :type last_seen_at: datetime
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.first_seen_at = first_seen_at
        self_.last_seen_at = last_seen_at
