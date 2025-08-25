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
    from datadog_api_client.v2.model.org_connection_org_relationship import OrgConnectionOrgRelationship


class OrgConnectionCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_org_relationship import OrgConnectionOrgRelationship

        return {
            "sink_org": (OrgConnectionOrgRelationship,),
        }

    attribute_map = {
        "sink_org": "sink_org",
    }

    def __init__(self_, sink_org: OrgConnectionOrgRelationship, **kwargs):
        """
        Relationships for org connection creation.

        :param sink_org: Org relationship.
        :type sink_org: OrgConnectionOrgRelationship
        """
        super().__init__(kwargs)

        self_.sink_org = sink_org
