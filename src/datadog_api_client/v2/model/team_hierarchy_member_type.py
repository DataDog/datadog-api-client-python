# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamHierarchyMemberType(ModelSimple):
    """
    Team hierarchy membership resource type.

    :param value: If omitted defaults to "user_team_relationship". Must be one of ["user_team_relationship"].
    :type value: str
    """

    allowed_values = {
        "user_team_relationship",
    }
    USER_TEAM_RELATIONSHIP: ClassVar["TeamHierarchyMemberType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamHierarchyMemberType.USER_TEAM_RELATIONSHIP = TeamHierarchyMemberType("user_team_relationship")
