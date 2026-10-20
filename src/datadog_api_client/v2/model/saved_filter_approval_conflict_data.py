# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.saved_filter_approval_conflict_attributes import (
        SavedFilterApprovalConflictAttributes,
    )
    from datadog_api_client.v2.model.saved_filter_approval_conflict_type import SavedFilterApprovalConflictType


class SavedFilterApprovalConflictData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_approval_conflict_attributes import (
            SavedFilterApprovalConflictAttributes,
        )
        from datadog_api_client.v2.model.saved_filter_approval_conflict_type import SavedFilterApprovalConflictType

        return {
            "attributes": (SavedFilterApprovalConflictAttributes,),
            "id": (UUID,),
            "type": (SavedFilterApprovalConflictType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SavedFilterApprovalConflictAttributes,
        id: UUID,
        type: SavedFilterApprovalConflictType,
        **kwargs,
    ):
        """
        One or more feature flags that reference this saved filter require approval for the rule update.

        :param attributes: One or more feature flags that reference this saved filter require approval for the rule update.
        :type attributes: SavedFilterApprovalConflictAttributes

        :param id: The ID of the saved filter.
        :type id: UUID

        :param type: The resource type for this saved filter update error.
        :type type: SavedFilterApprovalConflictType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
