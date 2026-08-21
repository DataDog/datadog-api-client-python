# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType


class TeamsOwnershipMappingBatchResultDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType

        return {
            "application_id": (UUID,),
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
        created_at: datetime,
        created_by: str,
        match_type: TeamsOwnershipMatchType,
        org_id: int,
        team_handle: str,
        view_name: str,
        application_id: Union[UUID, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a mapping created by an ``add`` operation.

        :param application_id: The ID of the RUM application, when one was provided.
        :type application_id: UUID, optional

        :param created_at: Timestamp when the mapping was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the mapping.
        :type created_by: str

        :param match_type: How the ``view_name`` is matched against RUM view names.
        :type match_type: TeamsOwnershipMatchType

        :param org_id: The ID of the organization that owns this mapping.
        :type org_id: int

        :param service: The RUM application's service name, when one was provided.
        :type service: str, optional

        :param team_handle: The handle of the team that owns the matched RUM views.
        :type team_handle: str

        :param view_name: The RUM view name to match, or its prefix when ``match_type`` is ``prefix``.
        :type view_name: str
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.match_type = match_type
        self_.org_id = org_id
        self_.team_handle = team_handle
        self_.view_name = view_name
