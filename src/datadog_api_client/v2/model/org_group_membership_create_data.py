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
    from datadog_api_client.v2.model.org_group_membership_create_attributes import OrgGroupMembershipCreateAttributes
    from datadog_api_client.v2.model.org_group_membership_create_relationships import (
        OrgGroupMembershipCreateRelationships,
    )
    from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType


class OrgGroupMembershipCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_membership_create_attributes import (
            OrgGroupMembershipCreateAttributes,
        )
        from datadog_api_client.v2.model.org_group_membership_create_relationships import (
            OrgGroupMembershipCreateRelationships,
        )
        from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType

        return {
            "attributes": (OrgGroupMembershipCreateAttributes,),
            "relationships": (OrgGroupMembershipCreateRelationships,),
            "type": (OrgGroupMembershipType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupMembershipCreateAttributes,
        relationships: OrgGroupMembershipCreateRelationships,
        type: OrgGroupMembershipType,
        **kwargs,
    ):
        """
        Data for adding organizations to an org group.

        :param attributes: Attributes for adding organizations to an org group.
        :type attributes: OrgGroupMembershipCreateAttributes

        :param relationships: Relationships for adding organizations to an org group.
        :type relationships: OrgGroupMembershipCreateRelationships

        :param type: Org group memberships resource type.
        :type type: OrgGroupMembershipType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
