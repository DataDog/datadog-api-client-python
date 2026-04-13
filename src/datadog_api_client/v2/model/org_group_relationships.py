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
    from datadog_api_client.v2.model.org_group_memberships_relationship import OrgGroupMembershipsRelationship


class OrgGroupRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_memberships_relationship import OrgGroupMembershipsRelationship

        return {
            "memberships": (OrgGroupMembershipsRelationship,),
        }

    attribute_map = {
        "memberships": "memberships",
    }

    def __init__(self_, memberships: Union[OrgGroupMembershipsRelationship, UnsetType] = unset, **kwargs):
        """
        Relationships of an org group.

        :param memberships: Relationship to org group memberships.
        :type memberships: OrgGroupMembershipsRelationship, optional
        """
        if memberships is not unset:
            kwargs["memberships"] = memberships
        super().__init__(kwargs)
