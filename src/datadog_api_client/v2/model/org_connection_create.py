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
    from datadog_api_client.v2.model.org_connection_create_attributes import OrgConnectionCreateAttributes
    from datadog_api_client.v2.model.org_connection_create_relationships import OrgConnectionCreateRelationships
    from datadog_api_client.v2.model.org_connection_type import OrgConnectionType


class OrgConnectionCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_create_attributes import OrgConnectionCreateAttributes
        from datadog_api_client.v2.model.org_connection_create_relationships import OrgConnectionCreateRelationships
        from datadog_api_client.v2.model.org_connection_type import OrgConnectionType

        return {
            "attributes": (OrgConnectionCreateAttributes,),
            "relationships": (OrgConnectionCreateRelationships,),
            "type": (OrgConnectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgConnectionCreateAttributes,
        relationships: OrgConnectionCreateRelationships,
        type: OrgConnectionType,
        **kwargs,
    ):
        """
        Org connection creation data.

        :param attributes: Attributes for creating an org connection.
        :type attributes: OrgConnectionCreateAttributes

        :param relationships: Relationships for org connection creation.
        :type relationships: OrgConnectionCreateRelationships

        :param type: Org connection type.
        :type type: OrgConnectionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
