# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_hierarchy_link_create import TeamHierarchyLinkCreate


class TeamHierarchyLinkCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_hierarchy_link_create import TeamHierarchyLinkCreate

        return {
            "data": (TeamHierarchyLinkCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TeamHierarchyLinkCreate, **kwargs):
        """
        Request to create a team hierarchy link

        :param data: Data provided when creating a team hierarchy link
        :type data: TeamHierarchyLinkCreate
        """
        super().__init__(kwargs)

        self_.data = data
