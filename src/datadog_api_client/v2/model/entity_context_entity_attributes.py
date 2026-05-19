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
    from datadog_api_client.v2.model.entity_context_revision import EntityContextRevision


class EntityContextEntityAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_revision import EntityContextRevision

        return {
            "revisions": ([EntityContextRevision],),
        }

    attribute_map = {
        "revisions": "revisions",
    }

    def __init__(self_, revisions: List[EntityContextRevision], **kwargs):
        """
        The attributes of an entity context entry, grouping all the historical revisions of the entity.

        :param revisions: The historical revisions of the entity, ordered chronologically.
        :type revisions: [EntityContextRevision]
        """
        super().__init__(kwargs)

        self_.revisions = revisions
