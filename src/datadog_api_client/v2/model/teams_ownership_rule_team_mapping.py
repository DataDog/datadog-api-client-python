# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TeamsOwnershipRuleTeamMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "mapping_id": (str,),
            "team_handle": (str,),
        }

    attribute_map = {
        "mapping_id": "mapping_id",
        "team_handle": "team_handle",
    }

    def __init__(self_, mapping_id: str, team_handle: str, **kwargs):
        """
        An individual team's ownership entry within a teams ownership rule.

        :param mapping_id: The ID of the underlying mapping, used to delete this team's ownership individually.
        :type mapping_id: str

        :param team_handle: The handle of the owning team.
        :type team_handle: str
        """
        super().__init__(kwargs)

        self_.mapping_id = mapping_id
        self_.team_handle = team_handle
