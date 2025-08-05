# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamSyncBulkType(ModelSimple):
    """
    Team sync bulk type.

    :param value: If omitted defaults to "team_sync_bulk". Must be one of ["team_sync_bulk"].
    :type value: str
    """

    allowed_values = {
        "team_sync_bulk",
    }
    TEAM_SYNC_BULK: ClassVar["TeamSyncBulkType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamSyncBulkType.TEAM_SYNC_BULK = TeamSyncBulkType("team_sync_bulk")
