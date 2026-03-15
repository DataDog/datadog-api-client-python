# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamSyncSelectionStateExternalIdType(ModelSimple):
    """
    The type of external identifier for the selection state item.
        For GitHub synchronization, the allowed values are `team` and
        `organization`.

    :param value: Must be one of ["team", "organization"].
    :type value: str
    """

    allowed_values = {
        "team",
        "organization",
    }
    TEAM: ClassVar["TeamSyncSelectionStateExternalIdType"]
    ORGANIZATION: ClassVar["TeamSyncSelectionStateExternalIdType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamSyncSelectionStateExternalIdType.TEAM = TeamSyncSelectionStateExternalIdType("team")
TeamSyncSelectionStateExternalIdType.ORGANIZATION = TeamSyncSelectionStateExternalIdType("organization")
