# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType


class TeamsOwnershipMappingBatchOperationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType

        return {
            "application_id": (UUID,),
            "match_type": (TeamsOwnershipMatchType,),
            "service": (str,),
            "team_handle": (str,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "match_type": "match_type",
        "service": "service",
        "team_handle": "team_handle",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: Union[UUID, UnsetType] = unset,
        match_type: Union[TeamsOwnershipMatchType, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        team_handle: Union[str, UnsetType] = unset,
        view_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the mapping to add. ``team_handle`` and ``view_name`` are required
        when ``op`` is ``add``. At least one of ``service`` or ``application_id`` must be provided.

        :param application_id: The ID of the RUM application this mapping applies to.
            For browser applications, provide the real application UUID — the team is applied to the view regardless of service.
            For mobile applications, omit this field (or set it to the nil UUID ``00000000-0000-0000-0000-000000000000`` ) — the team is applied to the view and service combination across all applications.
        :type application_id: UUID, optional

        :param match_type: How the ``view_name`` is matched against RUM view names.
        :type match_type: TeamsOwnershipMatchType, optional

        :param service: The RUM application's service name. For browser applications, this is optional. For mobile applications, this is required and scopes the ownership to a specific service.
        :type service: str, optional

        :param team_handle: The handle of the team that owns the matched RUM views.
        :type team_handle: str, optional

        :param view_name: The RUM view name to match, or its prefix when ``match_type`` is ``prefix``.
        :type view_name: str, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if match_type is not unset:
            kwargs["match_type"] = match_type
        if service is not unset:
            kwargs["service"] = service
        if team_handle is not unset:
            kwargs["team_handle"] = team_handle
        if view_name is not unset:
            kwargs["view_name"] = view_name
        super().__init__(kwargs)
