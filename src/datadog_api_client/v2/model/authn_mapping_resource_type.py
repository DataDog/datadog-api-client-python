# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AuthNMappingResourceType(ModelSimple):
    """
    The type of resource being mapped to.

    :param value: Must be one of ["role", "team"].
    :type value: str
    """

    allowed_values = {
        "role",
        "team",
    }
    ROLE: ClassVar["AuthNMappingResourceType"]
    TEAM: ClassVar["AuthNMappingResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AuthNMappingResourceType.ROLE = AuthNMappingResourceType("role")
AuthNMappingResourceType.TEAM = AuthNMappingResourceType("team")
