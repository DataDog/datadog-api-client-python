# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType
    from datadog_api_client.v2.model.teams_ownership_rule_team_mapping import TeamsOwnershipRuleTeamMapping


class TeamsOwnershipRuleResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType
        from datadog_api_client.v2.model.teams_ownership_rule_team_mapping import TeamsOwnershipRuleTeamMapping

        return {
            "application_id": (str,),
            "match_type": (TeamsOwnershipMatchType,),
            "service": (str,),
            "teams": ([TeamsOwnershipRuleTeamMapping],),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "match_type": "match_type",
        "service": "service",
        "teams": "teams",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: str,
        match_type: TeamsOwnershipMatchType,
        service: str,
        teams: List[TeamsOwnershipRuleTeamMapping],
        view_name: str,
        **kwargs,
    ):
        """
        The attributes of a teams ownership rule.

        :param application_id: The ID of the RUM application this mapping applies to.
            For browser applications, this is the real application UUID.
            For mobile applications, this is the nil UUID ``00000000-0000-0000-0000-000000000000`` (wildcard), meaning the ownership applies across all applications.
        :type application_id: str

        :param match_type: How the ``view_name`` is matched against RUM view names.
        :type match_type: TeamsOwnershipMatchType

        :param service: The RUM application's service name. For browser applications, may be empty. For mobile applications, this is the service that scopes the ownership.
        :type service: str

        :param teams: The teams that own the matched views, each paired with the ID of its underlying mapping.
        :type teams: [TeamsOwnershipRuleTeamMapping]

        :param view_name: The RUM view name to match, or its prefix when ``match_type`` is ``prefix``.
        :type view_name: str
        """
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.match_type = match_type
        self_.service = service
        self_.teams = teams
        self_.view_name = view_name
