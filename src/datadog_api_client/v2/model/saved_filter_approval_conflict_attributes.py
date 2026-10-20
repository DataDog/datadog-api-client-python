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
    from datadog_api_client.v2.model.saved_filter_flag_reference import SavedFilterFlagReference


class SavedFilterApprovalConflictAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_flag_reference import SavedFilterFlagReference

        return {
            "approval_required_flags": ([SavedFilterFlagReference],),
            "message": (str,),
        }

    attribute_map = {
        "approval_required_flags": "approval_required_flags",
        "message": "message",
    }

    def __init__(self_, approval_required_flags: List[SavedFilterFlagReference], message: str, **kwargs):
        """
        One or more feature flags that reference this saved filter require approval for the rule update.

        :param approval_required_flags: Feature flags preventing this update.
        :type approval_required_flags: [SavedFilterFlagReference]

        :param message: The reason the saved filter update was rejected.
        :type message: str
        """
        super().__init__(kwargs)

        self_.approval_required_flags = approval_required_flags
        self_.message = message
