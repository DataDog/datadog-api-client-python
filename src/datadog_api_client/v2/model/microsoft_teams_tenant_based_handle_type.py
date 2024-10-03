# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MicrosoftTeamsTenantBasedHandleType(ModelSimple):
    """
    Specifies the tenant-based handle resource type.

    :param value: If omitted defaults to "tenant-based-handle". Must be one of ["tenant-based-handle"].
    :type value: str
    """

    allowed_values = {
        "tenant-based-handle",
    }
    TENANT_BASED_HANDLE: ClassVar["MicrosoftTeamsTenantBasedHandleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MicrosoftTeamsTenantBasedHandleType.TENANT_BASED_HANDLE = MicrosoftTeamsTenantBasedHandleType("tenant-based-handle")
