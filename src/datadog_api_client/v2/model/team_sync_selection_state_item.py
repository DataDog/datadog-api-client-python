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
    from datadog_api_client.v2.model.team_sync_selection_state_external_id import TeamSyncSelectionStateExternalId
    from datadog_api_client.v2.model.team_sync_selection_state_operation import TeamSyncSelectionStateOperation
    from datadog_api_client.v2.model.team_sync_selection_state_scope import TeamSyncSelectionStateScope


class TeamSyncSelectionStateItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_sync_selection_state_external_id import TeamSyncSelectionStateExternalId
        from datadog_api_client.v2.model.team_sync_selection_state_operation import TeamSyncSelectionStateOperation
        from datadog_api_client.v2.model.team_sync_selection_state_scope import TeamSyncSelectionStateScope

        return {
            "external_id": (TeamSyncSelectionStateExternalId,),
            "operation": (TeamSyncSelectionStateOperation,),
            "scope": (TeamSyncSelectionStateScope,),
        }

    attribute_map = {
        "external_id": "external_id",
        "operation": "operation",
        "scope": "scope",
    }

    def __init__(
        self_,
        external_id: TeamSyncSelectionStateExternalId,
        operation: Union[TeamSyncSelectionStateOperation, UnsetType] = unset,
        scope: Union[TeamSyncSelectionStateScope, UnsetType] = unset,
        **kwargs,
    ):
        """
        Identifies a team or organization hierarchy to include in synchronization.

        :param external_id: The external identifier for a team or organization in the source platform.
        :type external_id: TeamSyncSelectionStateExternalId

        :param operation: The operation to perform on the selected hierarchy.
            When set to ``include`` , synchronization covers the
            referenced teams or organizations.
        :type operation: TeamSyncSelectionStateOperation, optional

        :param scope: The scope of the selection. When set to ``subtree`` ,
            synchronization includes the referenced team or
            organization and everything nested under it.
        :type scope: TeamSyncSelectionStateScope, optional
        """
        if operation is not unset:
            kwargs["operation"] = operation
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.external_id = external_id
