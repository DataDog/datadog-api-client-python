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


class OrgGroupMembershipRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne

        return {
            "org_group": (OrgGroupRelationshipToOne,),
        }

    attribute_map = {
        "org_group": "org_group",
    }

    def __init__(self_, org_group: Union[OrgGroupRelationshipToOne, UnsetType] = unset, **kwargs):
        """
        Relationships of an org group membership.

        :param org_group: Relationship to a single org group.
        :type org_group: OrgGroupRelationshipToOne, optional
        """
        if org_group is not unset:
            kwargs["org_group"] = org_group
        super().__init__(kwargs)
