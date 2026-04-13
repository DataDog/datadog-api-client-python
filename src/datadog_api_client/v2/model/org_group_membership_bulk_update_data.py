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
    from datadog_api_client.v2.model.org_group_membership_bulk_update_attributes import (
        OrgGroupMembershipBulkUpdateAttributes,
    )
    from datadog_api_client.v2.model.org_group_membership_bulk_update_relationships import (
        OrgGroupMembershipBulkUpdateRelationships,
    )
    from datadog_api_client.v2.model.org_group_membership_bulk_update_type import OrgGroupMembershipBulkUpdateType


class OrgGroupMembershipBulkUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_membership_bulk_update_attributes import (
            OrgGroupMembershipBulkUpdateAttributes,
        )
        from datadog_api_client.v2.model.org_group_membership_bulk_update_relationships import (
            OrgGroupMembershipBulkUpdateRelationships,
        )
        from datadog_api_client.v2.model.org_group_membership_bulk_update_type import OrgGroupMembershipBulkUpdateType

        return {
            "attributes": (OrgGroupMembershipBulkUpdateAttributes,),
            "relationships": (OrgGroupMembershipBulkUpdateRelationships,),
            "type": (OrgGroupMembershipBulkUpdateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupMembershipBulkUpdateAttributes,
        relationships: OrgGroupMembershipBulkUpdateRelationships,
        type: OrgGroupMembershipBulkUpdateType,
        **kwargs,
    ):
        """
        Data for bulk updating org group memberships.

        :param attributes: Attributes for bulk updating org group memberships.
        :type attributes: OrgGroupMembershipBulkUpdateAttributes

        :param relationships: Relationships for bulk updating memberships.
        :type relationships: OrgGroupMembershipBulkUpdateRelationships

        :param type: Org group membership bulk update resource type.
        :type type: OrgGroupMembershipBulkUpdateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
