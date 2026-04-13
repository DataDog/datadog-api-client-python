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
    from datadog_api_client.v2.model.org_group_policy_relationship_to_one import OrgGroupPolicyRelationshipToOne


class OrgGroupPolicyOverrideCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
        from datadog_api_client.v2.model.org_group_policy_relationship_to_one import OrgGroupPolicyRelationshipToOne

        return {
            "org_group": (OrgGroupRelationshipToOne,),
            "org_group_policy": (OrgGroupPolicyRelationshipToOne,),
        }

    attribute_map = {
        "org_group": "org_group",
        "org_group_policy": "org_group_policy",
    }

    def __init__(
        self_, org_group: OrgGroupRelationshipToOne, org_group_policy: OrgGroupPolicyRelationshipToOne, **kwargs
    ):
        """
        Relationships for creating a policy override.

        :param org_group: Relationship to a single org group.
        :type org_group: OrgGroupRelationshipToOne

        :param org_group_policy: Relationship to a single org group policy.
        :type org_group_policy: OrgGroupPolicyRelationshipToOne
        """
        super().__init__(kwargs)

        self_.org_group = org_group
        self_.org_group_policy = org_group_policy
