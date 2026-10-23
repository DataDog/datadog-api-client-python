# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageTargetRelationshipDataType(ModelSimple):
    """
    The resource type of the page target.

    :param value: Must be one of ["teams", "users", "cross_org_handles"].
    :type value: str
    """

    allowed_values = {
        "teams",
        "users",
        "cross_org_handles",
    }
    TEAMS: ClassVar["OnCallPageTargetRelationshipDataType"]
    USERS: ClassVar["OnCallPageTargetRelationshipDataType"]
    CROSS_ORG_HANDLES: ClassVar["OnCallPageTargetRelationshipDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageTargetRelationshipDataType.TEAMS = OnCallPageTargetRelationshipDataType("teams")
OnCallPageTargetRelationshipDataType.USERS = OnCallPageTargetRelationshipDataType("users")
OnCallPageTargetRelationshipDataType.CROSS_ORG_HANDLES = OnCallPageTargetRelationshipDataType("cross_org_handles")
