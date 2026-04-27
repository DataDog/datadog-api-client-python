# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.managed_orgs_relationships import ManagedOrgsRelationships
    from datadog_api_client.v2.model.managed_orgs_type import ManagedOrgsType


class ManagedOrgsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.managed_orgs_relationships import ManagedOrgsRelationships
        from datadog_api_client.v2.model.managed_orgs_type import ManagedOrgsType

        return {
            "id": (UUID,),
            "relationships": (ManagedOrgsRelationships,),
            "type": (ManagedOrgsType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self_, id: UUID, relationships: ManagedOrgsRelationships, type: ManagedOrgsType, **kwargs):
        """
        The managed organizations resource.

        :param id: The UUID of the current organization.
        :type id: UUID

        :param relationships: Relationships of the managed organizations resource.
        :type relationships: ManagedOrgsRelationships

        :param type: The resource type for managed organizations.
        :type type: ManagedOrgsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.relationships = relationships
        self_.type = type
