# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamHierarchyLinkType(ModelSimple):
    """
    Team hierarchy link type

    :param value: If omitted defaults to "team_hierarchy_links". Must be one of ["team_hierarchy_links"].
    :type value: str
    """

    allowed_values = {
        "team_hierarchy_links",
    }
    TEAM_HIERARCHY_LINKS: ClassVar["TeamHierarchyLinkType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamHierarchyLinkType.TEAM_HIERARCHY_LINKS = TeamHierarchyLinkType("team_hierarchy_links")
