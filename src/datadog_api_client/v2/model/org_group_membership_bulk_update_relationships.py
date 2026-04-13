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
    from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne


class OrgGroupMembershipBulkUpdateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne

        return {
            "source_org_group": (OrgGroupRelationshipToOne,),
            "target_org_group": (OrgGroupRelationshipToOne,),
        }

    attribute_map = {
        "source_org_group": "source_org_group",
        "target_org_group": "target_org_group",
    }

    def __init__(
        self_, source_org_group: OrgGroupRelationshipToOne, target_org_group: OrgGroupRelationshipToOne, **kwargs
    ):
        """
        Relationships for bulk updating memberships.

        :param source_org_group: Relationship to a single org group.
        :type source_org_group: OrgGroupRelationshipToOne

        :param target_org_group: Relationship to a single org group.
        :type target_org_group: OrgGroupRelationshipToOne
        """
        super().__init__(kwargs)

        self_.source_org_group = source_org_group
        self_.target_org_group = target_org_group
