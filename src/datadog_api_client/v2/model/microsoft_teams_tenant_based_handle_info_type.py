# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MicrosoftTeamsTenantBasedHandleInfoType(ModelSimple):
    """
    Tenant-based handle resource type.

    :param value: If omitted defaults to "ms-teams-tenant-based-handle-info". Must be one of ["ms-teams-tenant-based-handle-info"].
    :type value: str
    """

    allowed_values = {
        "ms-teams-tenant-based-handle-info",
    }
    MS_TEAMS_TENANT_BASED_HANDLE_INFO: ClassVar["MicrosoftTeamsTenantBasedHandleInfoType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MicrosoftTeamsTenantBasedHandleInfoType.MS_TEAMS_TENANT_BASED_HANDLE_INFO = MicrosoftTeamsTenantBasedHandleInfoType(
    "ms-teams-tenant-based-handle-info"
)
