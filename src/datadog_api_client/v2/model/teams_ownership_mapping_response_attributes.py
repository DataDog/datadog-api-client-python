# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType


class TeamsOwnershipMappingResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType

        return {
            "application_id": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "match_type": (TeamsOwnershipMatchType,),
            "org_id": (int,),
            "service": (str,),
            "team_handle": (str,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "created_at": "created_at",
        "created_by": "created_by",
        "match_type": "match_type",
        "org_id": "org_id",
        "service": "service",
        "team_handle": "team_handle",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: str,
        created_at: datetime,
        created_by: str,
        match_type: TeamsOwnershipMatchType,
        org_id: int,
        service: str,
        team_handle: str,
        view_name: str,
        **kwargs,
    ):
        """
        The attributes of a teams ownership mapping.

        :param application_id: The ID of the RUM application this mapping applies to.
            For browser applications, this is the real application UUID.
            For mobile applications, this is the nil UUID ``00000000-0000-0000-0000-000000000000`` (wildcard), meaning the ownership applies across all applications.
        :type application_id: str

        :param created_at: Timestamp when the mapping was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the mapping.
        :type created_by: str

        :param match_type: How the ``view_name`` is matched against RUM view names.
        :type match_type: TeamsOwnershipMatchType

        :param org_id: The ID of the organization that owns this mapping.
        :type org_id: int

        :param service: The RUM application's service name. For browser applications, may be empty. For mobile applications, this is the service that scopes the ownership.
        :type service: str

        :param team_handle: The handle of the team that owns the matched RUM views.
        :type team_handle: str

        :param view_name: The RUM view name to match, or its prefix when ``match_type`` is ``prefix``.
        :type view_name: str
        """
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.created_at = created_at
        self_.created_by = created_by
        self_.match_type = match_type
        self_.org_id = org_id
        self_.service = service
        self_.team_handle = team_handle
        self_.view_name = view_name
