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
    from datadog_api_client.v2.model.org_connection_attributes import OrgConnectionAttributes
    from datadog_api_client.v2.model.org_connection_relationships import OrgConnectionRelationships
    from datadog_api_client.v2.model.org_connection_type import OrgConnectionType


class OrgConnection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_attributes import OrgConnectionAttributes
        from datadog_api_client.v2.model.org_connection_relationships import OrgConnectionRelationships
        from datadog_api_client.v2.model.org_connection_type import OrgConnectionType

        return {
            "attributes": (OrgConnectionAttributes,),
            "id": (UUID,),
            "relationships": (OrgConnectionRelationships,),
            "type": (OrgConnectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgConnectionAttributes,
        id: UUID,
        relationships: OrgConnectionRelationships,
        type: OrgConnectionType,
        **kwargs,
    ):
        """
        An org connection.

        :param attributes: Org connection attributes.
        :type attributes: OrgConnectionAttributes

        :param id: The unique identifier of the org connection.
        :type id: UUID

        :param relationships: Related organizations and user.
        :type relationships: OrgConnectionRelationships

        :param type: Org connection type.
        :type type: OrgConnectionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
