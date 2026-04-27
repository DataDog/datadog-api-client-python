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
    from datadog_api_client.v2.model.org_resource_type import OrgResourceType


class OrgRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_resource_type import OrgResourceType

        return {
            "id": (UUID,),
            "type": (OrgResourceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: OrgResourceType, **kwargs):
        """
        Reference to an organization resource.

        :param id: The UUID of the organization.
        :type id: UUID

        :param type: The resource type for organizations.
        :type type: OrgResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
