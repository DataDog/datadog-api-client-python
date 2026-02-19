# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.change_request_object_attributes import ChangeRequestObjectAttributes
    from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
    from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType


class ChangeRequestResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_object_attributes import ChangeRequestObjectAttributes
        from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
        from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType

        return {
            "archived_at": (datetime, none_type),
            "attributes": (ChangeRequestObjectAttributes,),
            "change_request_linked_incident_uuid": (str,),
            "change_request_maintenance_window_query": (str,),
            "change_request_plan": (str,),
            "change_request_risk": (ChangeRequestRiskLevel,),
            "change_request_type": (ChangeRequestChangeType,),
            "closed_at": (datetime, none_type),
            "created_at": (datetime,),
            "creation_source": (str,),
            "description": (str,),
            "end_date": (datetime,),
            "key": (str,),
            "modified_at": (datetime,),
            "plan_notebook_id": (int,),
            "priority": (str,),
            "project_id": (str,),
            "start_date": (datetime,),
            "status": (str,),
            "title": (str,),
            "type": (str,),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "attributes": "attributes",
        "change_request_linked_incident_uuid": "change_request_linked_incident_uuid",
        "change_request_maintenance_window_query": "change_request_maintenance_window_query",
        "change_request_plan": "change_request_plan",
        "change_request_risk": "change_request_risk",
        "change_request_type": "change_request_type",
        "closed_at": "closed_at",
        "created_at": "created_at",
        "creation_source": "creation_source",
        "description": "description",
        "end_date": "end_date",
        "key": "key",
        "modified_at": "modified_at",
        "plan_notebook_id": "plan_notebook_id",
        "priority": "priority",
        "project_id": "project_id",
        "start_date": "start_date",
        "status": "status",
        "title": "title",
        "type": "type",
    }
    read_only_vars = {
        "archived_at",
        "closed_at",
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        attributes: ChangeRequestObjectAttributes,
        change_request_linked_incident_uuid: str,
        change_request_maintenance_window_query: str,
        change_request_plan: str,
        change_request_risk: ChangeRequestRiskLevel,
        change_request_type: ChangeRequestChangeType,
        created_at: datetime,
        creation_source: str,
        description: str,
        key: str,
        modified_at: datetime,
        plan_notebook_id: int,
        priority: str,
        project_id: str,
        status: str,
        title: str,
        type: str,
        archived_at: Union[datetime, none_type, UnsetType] = unset,
        closed_at: Union[datetime, none_type, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a change request response.

        :param archived_at: Timestamp of when the change request was archived.
        :type archived_at: datetime, none_type, optional

        :param attributes: Custom attributes of the change request as key-value pairs.
        :type attributes: ChangeRequestObjectAttributes

        :param change_request_linked_incident_uuid: The UUID of the linked incident.
        :type change_request_linked_incident_uuid: str

        :param change_request_maintenance_window_query: The maintenance window query for the change request.
        :type change_request_maintenance_window_query: str

        :param change_request_plan: The plan associated with the change request.
        :type change_request_plan: str

        :param change_request_risk: The risk level of the change request.
        :type change_request_risk: ChangeRequestRiskLevel

        :param change_request_type: The type of the change request.
        :type change_request_type: ChangeRequestChangeType

        :param closed_at: Timestamp of when the change request was closed.
        :type closed_at: datetime, none_type, optional

        :param created_at: Timestamp of when the change request was created.
        :type created_at: datetime

        :param creation_source: The source from which the change request was created.
        :type creation_source: str

        :param description: The description of the change request.
        :type description: str

        :param end_date: The planned end date of the change request.
        :type end_date: datetime, optional

        :param key: The human-readable key of the change request.
        :type key: str

        :param modified_at: Timestamp of when the change request was last modified.
        :type modified_at: datetime

        :param plan_notebook_id: The notebook ID associated with the change request plan.
        :type plan_notebook_id: int

        :param priority: The priority of the change request.
        :type priority: str

        :param project_id: The project UUID associated with the change request.
        :type project_id: str

        :param start_date: The planned start date of the change request.
        :type start_date: datetime, optional

        :param status: The current status of the change request.
        :type status: str

        :param title: The title of the change request.
        :type title: str

        :param type: The case type.
        :type type: str
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if closed_at is not unset:
            kwargs["closed_at"] = closed_at
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if start_date is not unset:
            kwargs["start_date"] = start_date
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.change_request_linked_incident_uuid = change_request_linked_incident_uuid
        self_.change_request_maintenance_window_query = change_request_maintenance_window_query
        self_.change_request_plan = change_request_plan
        self_.change_request_risk = change_request_risk
        self_.change_request_type = change_request_type
        self_.created_at = created_at
        self_.creation_source = creation_source
        self_.description = description
        self_.key = key
        self_.modified_at = modified_at
        self_.plan_notebook_id = plan_notebook_id
        self_.priority = priority
        self_.project_id = project_id
        self_.status = status
        self_.title = title
        self_.type = type
