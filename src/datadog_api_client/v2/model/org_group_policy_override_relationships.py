# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
    from datadog_api_client.v2.model.org_group_policy_relationship_to_one import OrgGroupPolicyRelationshipToOne


class OrgGroupPolicyOverrideRelationships(ModelNormal):
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
        self_,
        org_group: Union[OrgGroupRelationshipToOne, UnsetType] = unset,
        org_group_policy: Union[OrgGroupPolicyRelationshipToOne, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of an org group policy override.

        :param org_group: Relationship to a single org group.
        :type org_group: OrgGroupRelationshipToOne, optional

        :param org_group_policy: Relationship to a single org group policy.
        :type org_group_policy: OrgGroupPolicyRelationshipToOne, optional
        """
        if org_group is not unset:
            kwargs["org_group"] = org_group
        if org_group_policy is not unset:
            kwargs["org_group_policy"] = org_group_policy
        super().__init__(kwargs)
