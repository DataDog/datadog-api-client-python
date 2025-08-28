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
    from datadog_api_client.v2.model.org_connection_user_relationship import OrgConnectionUserRelationship
    from datadog_api_client.v2.model.org_connection_org_relationship import OrgConnectionOrgRelationship


class OrgConnectionRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_user_relationship import OrgConnectionUserRelationship
        from datadog_api_client.v2.model.org_connection_org_relationship import OrgConnectionOrgRelationship

        return {
            "created_by": (OrgConnectionUserRelationship,),
            "sink_org": (OrgConnectionOrgRelationship,),
            "source_org": (OrgConnectionOrgRelationship,),
        }

    attribute_map = {
        "created_by": "created_by",
        "sink_org": "sink_org",
        "source_org": "source_org",
    }

    def __init__(
        self_,
        created_by: Union[OrgConnectionUserRelationship, UnsetType] = unset,
        sink_org: Union[OrgConnectionOrgRelationship, UnsetType] = unset,
        source_org: Union[OrgConnectionOrgRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Related organizations and user.

        :param created_by: User relationship.
        :type created_by: OrgConnectionUserRelationship, optional

        :param sink_org: Org relationship.
        :type sink_org: OrgConnectionOrgRelationship, optional

        :param source_org: Org relationship.
        :type source_org: OrgConnectionOrgRelationship, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if sink_org is not unset:
            kwargs["sink_org"] = sink_org
        if source_org is not unset:
            kwargs["source_org"] = source_org
        super().__init__(kwargs)
