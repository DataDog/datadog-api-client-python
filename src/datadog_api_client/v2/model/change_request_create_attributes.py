# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
    from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType


class ChangeRequestCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
        from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType

        return {
            "change_request_linked_incident_uuid": (str,),
            "change_request_maintenance_window_query": (str,),
            "change_request_plan": (str,),
            "change_request_risk": (ChangeRequestRiskLevel,),
            "change_request_type": (ChangeRequestChangeType,),
            "description": (str,),
            "end_date": (datetime,),
            "project_id": (str,),
            "requested_teams": ([str],),
            "start_date": (datetime,),
            "title": (str,),
        }

    attribute_map = {
        "change_request_linked_incident_uuid": "change_request_linked_incident_uuid",
        "change_request_maintenance_window_query": "change_request_maintenance_window_query",
        "change_request_plan": "change_request_plan",
        "change_request_risk": "change_request_risk",
        "change_request_type": "change_request_type",
        "description": "description",
        "end_date": "end_date",
        "project_id": "project_id",
        "requested_teams": "requested_teams",
        "start_date": "start_date",
        "title": "title",
    }

    def __init__(
        self_,
        title: str,
        change_request_linked_incident_uuid: Union[str, UnsetType] = unset,
        change_request_maintenance_window_query: Union[str, UnsetType] = unset,
        change_request_plan: Union[str, UnsetType] = unset,
        change_request_risk: Union[ChangeRequestRiskLevel, UnsetType] = unset,
        change_request_type: Union[ChangeRequestChangeType, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        requested_teams: Union[List[str], UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a change request.

        :param change_request_linked_incident_uuid: The UUID of an incident to link to the change request.
        :type change_request_linked_incident_uuid: str, optional

        :param change_request_maintenance_window_query: The maintenance window query for the change request.
        :type change_request_maintenance_window_query: str, optional

        :param change_request_plan: The plan associated with the change request.
        :type change_request_plan: str, optional

        :param change_request_risk: The risk level of the change request.
        :type change_request_risk: ChangeRequestRiskLevel, optional

        :param change_request_type: The type of the change request.
        :type change_request_type: ChangeRequestChangeType, optional

        :param description: The description of the change request.
        :type description: str, optional

        :param end_date: The planned end date of the change request.
        :type end_date: datetime, optional

        :param project_id: The project UUID to associate with the change request.
        :type project_id: str, optional

        :param requested_teams: A list of team handles to request decisions from.
        :type requested_teams: [str], optional

        :param start_date: The planned start date of the change request.
        :type start_date: datetime, optional

        :param title: The title of the change request.
        :type title: str
        """
        if change_request_linked_incident_uuid is not unset:
            kwargs["change_request_linked_incident_uuid"] = change_request_linked_incident_uuid
        if change_request_maintenance_window_query is not unset:
            kwargs["change_request_maintenance_window_query"] = change_request_maintenance_window_query
        if change_request_plan is not unset:
            kwargs["change_request_plan"] = change_request_plan
        if change_request_risk is not unset:
            kwargs["change_request_risk"] = change_request_risk
        if change_request_type is not unset:
            kwargs["change_request_type"] = change_request_type
        if description is not unset:
            kwargs["description"] = description
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if project_id is not unset:
            kwargs["project_id"] = project_id
        if requested_teams is not unset:
            kwargs["requested_teams"] = requested_teams
        if start_date is not unset:
            kwargs["start_date"] = start_date
        super().__init__(kwargs)

        self_.title = title
