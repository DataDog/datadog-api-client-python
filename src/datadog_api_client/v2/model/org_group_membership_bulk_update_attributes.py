# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.global_org_identifier import GlobalOrgIdentifier


class OrgGroupMembershipBulkUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_org_identifier import GlobalOrgIdentifier

        return {
            "orgs": ([GlobalOrgIdentifier],),
        }

    attribute_map = {
        "orgs": "orgs",
    }

    def __init__(self_, orgs: List[GlobalOrgIdentifier], **kwargs):
        """
        Attributes for bulk updating org group memberships.

        :param orgs: List of organizations to move. Maximum 100 per request.
        :type orgs: [GlobalOrgIdentifier]
        """
        super().__init__(kwargs)

        self_.orgs = orgs
