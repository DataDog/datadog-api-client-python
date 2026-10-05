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
    from datadog_api_client.v2.model.org_group_membership_bulk_delete_request_data import (
        OrgGroupMembershipBulkDeleteRequestData,
    )


class OrgGroupMembershipBulkDeleteRequest(ModelNormal):
    validations = {
        "data": {
            "max_items": 100,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_membership_bulk_delete_request_data import (
            OrgGroupMembershipBulkDeleteRequestData,
        )

        return {
            "data": ([OrgGroupMembershipBulkDeleteRequestData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[OrgGroupMembershipBulkDeleteRequestData], **kwargs):
        """
        Request to delete a batch of org group memberships.

        :param data: The memberships to delete, as membership resource identifiers. Between 1 and 100 unique membership IDs per request.
        :type data: [OrgGroupMembershipBulkDeleteRequestData]
        """
        super().__init__(kwargs)

        self_.data = data
