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
    from datadog_api_client.v2.model.org_group_membership_bulk_update_data import OrgGroupMembershipBulkUpdateData


class OrgGroupMembershipBulkUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_membership_bulk_update_data import OrgGroupMembershipBulkUpdateData

        return {
            "data": (OrgGroupMembershipBulkUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OrgGroupMembershipBulkUpdateData, **kwargs):
        """
        Request to bulk update org group memberships.

        :param data: Data for bulk updating org group memberships.
        :type data: OrgGroupMembershipBulkUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
