# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import (
        IncidentTimelineCellCreateAttributes,
    )
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
    from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
    from datadog_api_client.v2.model.incident_field_attributes_multiple_value import (
        IncidentFieldAttributesMultipleValue,
    )
    from datadog_api_client.v2.model.incident_timeline_cell_markdown_create_attributes import (
        IncidentTimelineCellMarkdownCreateAttributes,
    )


class IncidentCreateAttributes(ModelNormal):
    validations = {
        "case_id": {
            "inclusive_maximum": 2147483647,
            "inclusive_minimum": 0,
        },
        "duration": {
            "inclusive_maximum": 2147483647,
        },
        "public_id": {
            "inclusive_maximum": 2147483647,
        },
        "time_to_resolve": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
        from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import (
            IncidentTimelineCellCreateAttributes,
        )
        from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle

        return {
            "additional_notifications": (str, none_type),
            "archived": (datetime, none_type),
            "case_id": (int, none_type),
            "creation_idempotency_key": (str, none_type),
            "customer_impact_end": (datetime, none_type),
            "customer_impact_scope": (str,),
            "customer_impact_start": (datetime, none_type),
            "customer_impacted": (bool,),
            "detected": (datetime, none_type),
            "duration": (int, none_type),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "incident_type_uuid": (str, none_type),
            "initial_cells": ([IncidentTimelineCellCreateAttributes],),
            "notification_handles": ([IncidentNotificationHandle],),
            "public_id": (int, none_type),
            "resolved": (datetime, none_type),
            "severity": (str, none_type),
            "state": (str, none_type),
            "time_to_resolve": (int, none_type),
            "title": (str,),
        }

    attribute_map = {
        "additional_notifications": "additional_notifications",
        "archived": "archived",
        "case_id": "case_id",
        "creation_idempotency_key": "creation_idempotency_key",
        "customer_impact_end": "customer_impact_end",
        "customer_impact_scope": "customer_impact_scope",
        "customer_impact_start": "customer_impact_start",
        "customer_impacted": "customer_impacted",
        "detected": "detected",
        "duration": "duration",
        "fields": "fields",
        "incident_type_uuid": "incident_type_uuid",
        "initial_cells": "initial_cells",
        "notification_handles": "notification_handles",
        "public_id": "public_id",
        "resolved": "resolved",
        "severity": "severity",
        "state": "state",
        "time_to_resolve": "time_to_resolve",
        "title": "title",
    }

    def __init__(
        self_,
        customer_impacted: bool,
        title: str,
        additional_notifications: Union[str, none_type, UnsetType] = unset,
        archived: Union[datetime, none_type, UnsetType] = unset,
        case_id: Union[int, none_type, UnsetType] = unset,
        creation_idempotency_key: Union[str, none_type, UnsetType] = unset,
        customer_impact_end: Union[datetime, none_type, UnsetType] = unset,
        customer_impact_scope: Union[str, UnsetType] = unset,
        customer_impact_start: Union[datetime, none_type, UnsetType] = unset,
        detected: Union[datetime, none_type, UnsetType] = unset,
        duration: Union[int, none_type, UnsetType] = unset,
        fields: Union[
            Dict[
                str,
                Union[
                    IncidentFieldAttributes, IncidentFieldAttributesSingleValue, IncidentFieldAttributesMultipleValue
                ],
            ],
            UnsetType,
        ] = unset,
        incident_type_uuid: Union[str, none_type, UnsetType] = unset,
        initial_cells: Union[
            List[Union[IncidentTimelineCellCreateAttributes, IncidentTimelineCellMarkdownCreateAttributes]], UnsetType
        ] = unset,
        notification_handles: Union[List[IncidentNotificationHandle], UnsetType] = unset,
        public_id: Union[int, none_type, UnsetType] = unset,
        resolved: Union[datetime, none_type, UnsetType] = unset,
        severity: Union[str, none_type, UnsetType] = unset,
        state: Union[str, none_type, UnsetType] = unset,
        time_to_resolve: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident's attributes for a create request.

        :param additional_notifications: The IncidentCreateAttributes additional_notifications.
        :type additional_notifications: str, none_type, optional

        :param archived: The IncidentCreateAttributes archived.
        :type archived: datetime, none_type, optional

        :param case_id: The IncidentCreateAttributes case_id.
        :type case_id: int, none_type, optional

        :param creation_idempotency_key: The IncidentCreateAttributes creation_idempotency_key.
        :type creation_idempotency_key: str, none_type, optional

        :param customer_impact_end: The IncidentCreateAttributes customer_impact_end.
        :type customer_impact_end: datetime, none_type, optional

        :param customer_impact_scope: Required if ``customer_impacted:"true"``. A summary of the impact customers experienced during the incident.
        :type customer_impact_scope: str, optional

        :param customer_impact_start: The IncidentCreateAttributes customer_impact_start.
        :type customer_impact_start: datetime, none_type, optional

        :param customer_impacted: A flag indicating whether the incident caused customer impact.
        :type customer_impacted: bool

        :param detected: The IncidentCreateAttributes detected.
        :type detected: datetime, none_type, optional

        :param duration: The IncidentCreateAttributes duration.
        :type duration: int, none_type, optional

        :param fields: A condensed view of the user-defined fields for which to create initial selections.
        :type fields: {str: (IncidentFieldAttributes,)}, optional

        :param incident_type_uuid: The IncidentCreateAttributes incident_type_uuid.
        :type incident_type_uuid: str, none_type, optional

        :param initial_cells: An array of initial timeline cells to be placed at the beginning of the incident timeline.
        :type initial_cells: [IncidentTimelineCellCreateAttributes], optional

        :param notification_handles: Notification handles that will be notified of the incident at creation.
        :type notification_handles: [IncidentNotificationHandle], optional

        :param public_id: The IncidentCreateAttributes public_id.
        :type public_id: int, none_type, optional

        :param resolved: The IncidentCreateAttributes resolved.
        :type resolved: datetime, none_type, optional

        :param severity: The IncidentCreateAttributes severity.
        :type severity: str, none_type, optional

        :param state: The IncidentCreateAttributes state.
        :type state: str, none_type, optional

        :param time_to_resolve: The IncidentCreateAttributes time_to_resolve.
        :type time_to_resolve: int, none_type, optional

        :param title: The title of the incident, which summarizes what happened.
        :type title: str
        """
        if additional_notifications is not unset:
            kwargs["additional_notifications"] = additional_notifications
        if archived is not unset:
            kwargs["archived"] = archived
        if case_id is not unset:
            kwargs["case_id"] = case_id
        if creation_idempotency_key is not unset:
            kwargs["creation_idempotency_key"] = creation_idempotency_key
        if customer_impact_end is not unset:
            kwargs["customer_impact_end"] = customer_impact_end
        if customer_impact_scope is not unset:
            kwargs["customer_impact_scope"] = customer_impact_scope
        if customer_impact_start is not unset:
            kwargs["customer_impact_start"] = customer_impact_start
        if detected is not unset:
            kwargs["detected"] = detected
        if duration is not unset:
            kwargs["duration"] = duration
        if fields is not unset:
            kwargs["fields"] = fields
        if incident_type_uuid is not unset:
            kwargs["incident_type_uuid"] = incident_type_uuid
        if initial_cells is not unset:
            kwargs["initial_cells"] = initial_cells
        if notification_handles is not unset:
            kwargs["notification_handles"] = notification_handles
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if resolved is not unset:
            kwargs["resolved"] = resolved
        if severity is not unset:
            kwargs["severity"] = severity
        if state is not unset:
            kwargs["state"] = state
        if time_to_resolve is not unset:
            kwargs["time_to_resolve"] = time_to_resolve
        super().__init__(kwargs)

        self_.customer_impacted = customer_impacted
        self_.title = title
