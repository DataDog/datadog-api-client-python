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
    from datadog_api_client.v2.model.incident_non_datadog_creator import IncidentNonDatadogCreator
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
    from datadog_api_client.v2.model.incident_severity import IncidentSeverity
    from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
    from datadog_api_client.v2.model.incident_field_attributes_multiple_value import (
        IncidentFieldAttributesMultipleValue,
    )


class IncidentResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
        from datadog_api_client.v2.model.incident_non_datadog_creator import IncidentNonDatadogCreator
        from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
        from datadog_api_client.v2.model.incident_severity import IncidentSeverity

        return {
            "archived": (datetime, none_type),
            "case_id": (int, none_type),
            "created": (datetime,),
            "customer_impact_duration": (int,),
            "customer_impact_end": (datetime, none_type),
            "customer_impact_scope": (str, none_type),
            "customer_impact_start": (datetime, none_type),
            "customer_impacted": (bool,),
            "detected": (datetime, none_type),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "incident_type_uuid": (str,),
            "is_test": (bool,),
            "modified": (datetime,),
            "non_datadog_creator": (IncidentNonDatadogCreator,),
            "notification_handles": ([IncidentNotificationHandle], none_type),
            "public_id": (int,),
            "resolved": (datetime, none_type),
            "severity": (IncidentSeverity,),
            "state": (str, none_type),
            "time_to_detect": (int,),
            "time_to_internal_response": (int,),
            "time_to_repair": (int,),
            "time_to_resolve": (int,),
            "title": (str,),
            "visibility": (str, none_type),
        }

    attribute_map = {
        "archived": "archived",
        "case_id": "case_id",
        "created": "created",
        "customer_impact_duration": "customer_impact_duration",
        "customer_impact_end": "customer_impact_end",
        "customer_impact_scope": "customer_impact_scope",
        "customer_impact_start": "customer_impact_start",
        "customer_impacted": "customer_impacted",
        "detected": "detected",
        "fields": "fields",
        "incident_type_uuid": "incident_type_uuid",
        "is_test": "is_test",
        "modified": "modified",
        "non_datadog_creator": "non_datadog_creator",
        "notification_handles": "notification_handles",
        "public_id": "public_id",
        "resolved": "resolved",
        "severity": "severity",
        "state": "state",
        "time_to_detect": "time_to_detect",
        "time_to_internal_response": "time_to_internal_response",
        "time_to_repair": "time_to_repair",
        "time_to_resolve": "time_to_resolve",
        "title": "title",
        "visibility": "visibility",
    }
    read_only_vars = {
        "archived",
        "created",
        "customer_impact_duration",
        "modified",
        "time_to_detect",
        "time_to_internal_response",
        "time_to_repair",
        "time_to_resolve",
    }

    def __init__(
        self_,
        title: str,
        archived: Union[datetime, none_type, UnsetType] = unset,
        case_id: Union[int, none_type, UnsetType] = unset,
        created: Union[datetime, UnsetType] = unset,
        customer_impact_duration: Union[int, UnsetType] = unset,
        customer_impact_end: Union[datetime, none_type, UnsetType] = unset,
        customer_impact_scope: Union[str, none_type, UnsetType] = unset,
        customer_impact_start: Union[datetime, none_type, UnsetType] = unset,
        customer_impacted: Union[bool, UnsetType] = unset,
        detected: Union[datetime, none_type, UnsetType] = unset,
        fields: Union[
            Dict[
                str,
                Union[
                    IncidentFieldAttributes, IncidentFieldAttributesSingleValue, IncidentFieldAttributesMultipleValue
                ],
            ],
            UnsetType,
        ] = unset,
        incident_type_uuid: Union[str, UnsetType] = unset,
        is_test: Union[bool, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        non_datadog_creator: Union[IncidentNonDatadogCreator, none_type, UnsetType] = unset,
        notification_handles: Union[List[IncidentNotificationHandle], none_type, UnsetType] = unset,
        public_id: Union[int, UnsetType] = unset,
        resolved: Union[datetime, none_type, UnsetType] = unset,
        severity: Union[IncidentSeverity, UnsetType] = unset,
        state: Union[str, none_type, UnsetType] = unset,
        time_to_detect: Union[int, UnsetType] = unset,
        time_to_internal_response: Union[int, UnsetType] = unset,
        time_to_repair: Union[int, UnsetType] = unset,
        time_to_resolve: Union[int, UnsetType] = unset,
        visibility: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident's attributes from a response.

        :param archived: Timestamp of when the incident was archived.
        :type archived: datetime, none_type, optional

        :param case_id: The incident case id.
        :type case_id: int, none_type, optional

        :param created: Timestamp when the incident was created.
        :type created: datetime, optional

        :param customer_impact_duration: Length of the incident's customer impact in seconds.
            Equals the difference between ``customer_impact_start`` and ``customer_impact_end``.
        :type customer_impact_duration: int, optional

        :param customer_impact_end: Timestamp when customers were no longer impacted by the incident.
        :type customer_impact_end: datetime, none_type, optional

        :param customer_impact_scope: A summary of the impact customers experienced during the incident.
        :type customer_impact_scope: str, none_type, optional

        :param customer_impact_start: Timestamp when customers began being impacted by the incident.
        :type customer_impact_start: datetime, none_type, optional

        :param customer_impacted: A flag indicating whether the incident caused customer impact.
        :type customer_impacted: bool, optional

        :param detected: Timestamp when the incident was detected.
        :type detected: datetime, none_type, optional

        :param fields: A condensed view of the user-defined fields attached to incidents.
        :type fields: {str: (IncidentFieldAttributes,)}, optional

        :param incident_type_uuid: A unique identifier that represents an incident type.
        :type incident_type_uuid: str, optional

        :param is_test: A flag indicating whether the incident is a test incident.
        :type is_test: bool, optional

        :param modified: Timestamp when the incident was last modified.
        :type modified: datetime, optional

        :param non_datadog_creator: Incident's non Datadog creator.
        :type non_datadog_creator: IncidentNonDatadogCreator, none_type, optional

        :param notification_handles: Notification handles that will be notified of the incident during update.
        :type notification_handles: [IncidentNotificationHandle], none_type, optional

        :param public_id: The monotonically increasing integer ID for the incident.
        :type public_id: int, optional

        :param resolved: Timestamp when the incident's state was last changed from active or stable to resolved or completed.
        :type resolved: datetime, none_type, optional

        :param severity: The incident severity.
        :type severity: IncidentSeverity, optional

        :param state: The state incident.
        :type state: str, none_type, optional

        :param time_to_detect: The amount of time in seconds to detect the incident.
            Equals the difference between ``customer_impact_start`` and ``detected``.
        :type time_to_detect: int, optional

        :param time_to_internal_response: The amount of time in seconds to call incident after detection. Equals the difference of ``detected`` and ``created``.
        :type time_to_internal_response: int, optional

        :param time_to_repair: The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between ``customer_impact_end`` and ``detected``.
        :type time_to_repair: int, optional

        :param time_to_resolve: The amount of time in seconds to resolve the incident after it was created. Equals the difference between ``created`` and ``resolved``.
        :type time_to_resolve: int, optional

        :param title: The title of the incident, which summarizes what happened.
        :type title: str

        :param visibility: The incident visibility status.
        :type visibility: str, none_type, optional
        """
        if archived is not unset:
            kwargs["archived"] = archived
        if case_id is not unset:
            kwargs["case_id"] = case_id
        if created is not unset:
            kwargs["created"] = created
        if customer_impact_duration is not unset:
            kwargs["customer_impact_duration"] = customer_impact_duration
        if customer_impact_end is not unset:
            kwargs["customer_impact_end"] = customer_impact_end
        if customer_impact_scope is not unset:
            kwargs["customer_impact_scope"] = customer_impact_scope
        if customer_impact_start is not unset:
            kwargs["customer_impact_start"] = customer_impact_start
        if customer_impacted is not unset:
            kwargs["customer_impacted"] = customer_impacted
        if detected is not unset:
            kwargs["detected"] = detected
        if fields is not unset:
            kwargs["fields"] = fields
        if incident_type_uuid is not unset:
            kwargs["incident_type_uuid"] = incident_type_uuid
        if is_test is not unset:
            kwargs["is_test"] = is_test
        if modified is not unset:
            kwargs["modified"] = modified
        if non_datadog_creator is not unset:
            kwargs["non_datadog_creator"] = non_datadog_creator
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
        if time_to_detect is not unset:
            kwargs["time_to_detect"] = time_to_detect
        if time_to_internal_response is not unset:
            kwargs["time_to_internal_response"] = time_to_internal_response
        if time_to_repair is not unset:
            kwargs["time_to_repair"] = time_to_repair
        if time_to_resolve is not unset:
            kwargs["time_to_resolve"] = time_to_resolve
        if visibility is not unset:
            kwargs["visibility"] = visibility
        super().__init__(kwargs)

        self_.title = title
