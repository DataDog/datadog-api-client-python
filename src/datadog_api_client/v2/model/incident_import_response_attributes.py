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


class IncidentImportResponseAttributes(ModelNormal):
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
            "created_by_uuid": (str, none_type),
            "creation_idempotency_key": (str, none_type),
            "customer_impact_end": (datetime, none_type),
            "customer_impact_scope": (str, none_type),
            "customer_impact_start": (datetime, none_type),
            "declared": (datetime, none_type),
            "declared_by_uuid": (str, none_type),
            "detected": (datetime, none_type),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "incident_type_uuid": (str,),
            "is_test": (bool,),
            "last_modified_by_uuid": (str, none_type),
            "modified": (datetime,),
            "non_datadog_creator": (IncidentNonDatadogCreator,),
            "notification_handles": ([IncidentNotificationHandle], none_type),
            "public_id": (int,),
            "resolved": (datetime, none_type),
            "severity": (IncidentSeverity,),
            "state": (str, none_type),
            "title": (str,),
            "visibility": (str, none_type),
        }

    attribute_map = {
        "archived": "archived",
        "case_id": "case_id",
        "created": "created",
        "created_by_uuid": "created_by_uuid",
        "creation_idempotency_key": "creation_idempotency_key",
        "customer_impact_end": "customer_impact_end",
        "customer_impact_scope": "customer_impact_scope",
        "customer_impact_start": "customer_impact_start",
        "declared": "declared",
        "declared_by_uuid": "declared_by_uuid",
        "detected": "detected",
        "fields": "fields",
        "incident_type_uuid": "incident_type_uuid",
        "is_test": "is_test",
        "last_modified_by_uuid": "last_modified_by_uuid",
        "modified": "modified",
        "non_datadog_creator": "non_datadog_creator",
        "notification_handles": "notification_handles",
        "public_id": "public_id",
        "resolved": "resolved",
        "severity": "severity",
        "state": "state",
        "title": "title",
        "visibility": "visibility",
    }
    read_only_vars = {
        "archived",
        "created",
        "modified",
    }

    def __init__(
        self_,
        title: str,
        archived: Union[datetime, none_type, UnsetType] = unset,
        case_id: Union[int, none_type, UnsetType] = unset,
        created: Union[datetime, UnsetType] = unset,
        created_by_uuid: Union[str, none_type, UnsetType] = unset,
        creation_idempotency_key: Union[str, none_type, UnsetType] = unset,
        customer_impact_end: Union[datetime, none_type, UnsetType] = unset,
        customer_impact_scope: Union[str, none_type, UnsetType] = unset,
        customer_impact_start: Union[datetime, none_type, UnsetType] = unset,
        declared: Union[datetime, none_type, UnsetType] = unset,
        declared_by_uuid: Union[str, none_type, UnsetType] = unset,
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
        last_modified_by_uuid: Union[str, none_type, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        non_datadog_creator: Union[IncidentNonDatadogCreator, none_type, UnsetType] = unset,
        notification_handles: Union[List[IncidentNotificationHandle], none_type, UnsetType] = unset,
        public_id: Union[int, UnsetType] = unset,
        resolved: Union[datetime, none_type, UnsetType] = unset,
        severity: Union[IncidentSeverity, UnsetType] = unset,
        state: Union[str, none_type, UnsetType] = unset,
        visibility: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident's attributes from an import response.

        :param archived: Timestamp when the incident was archived.
        :type archived: datetime, none_type, optional

        :param case_id: The incident case ID.
        :type case_id: int, none_type, optional

        :param created: Timestamp when the incident was created.
        :type created: datetime, optional

        :param created_by_uuid: UUID of the user who created the incident.
        :type created_by_uuid: str, none_type, optional

        :param creation_idempotency_key: A unique key used to ensure idempotent incident creation.
        :type creation_idempotency_key: str, none_type, optional

        :param customer_impact_end: Timestamp when customers were no longer impacted by the incident.
        :type customer_impact_end: datetime, none_type, optional

        :param customer_impact_scope: A summary of the impact customers experienced during the incident.
        :type customer_impact_scope: str, none_type, optional

        :param customer_impact_start: Timestamp when customers began to be impacted by the incident.
        :type customer_impact_start: datetime, none_type, optional

        :param declared: Timestamp when the incident was declared.
        :type declared: datetime, none_type, optional

        :param declared_by_uuid: UUID of the user who declared the incident.
        :type declared_by_uuid: str, none_type, optional

        :param detected: Timestamp when the incident was detected.
        :type detected: datetime, none_type, optional

        :param fields: A condensed view of the user-defined fields attached to incidents.
        :type fields: {str: (IncidentFieldAttributes,)}, optional

        :param incident_type_uuid: A unique identifier that represents an incident type.
        :type incident_type_uuid: str, optional

        :param is_test: A flag indicating whether the incident is a test incident.
        :type is_test: bool, optional

        :param last_modified_by_uuid: UUID of the user who last modified the incident.
        :type last_modified_by_uuid: str, none_type, optional

        :param modified: Timestamp when the incident was last modified.
        :type modified: datetime, optional

        :param non_datadog_creator: Incident's non Datadog creator.
        :type non_datadog_creator: IncidentNonDatadogCreator, none_type, optional

        :param notification_handles: Notification handles that are notified of the incident during update.
        :type notification_handles: [IncidentNotificationHandle], none_type, optional

        :param public_id: The monotonically increasing integer ID for the incident.
        :type public_id: int, optional

        :param resolved: Timestamp when the incident's state was last changed from active or stable to resolved or completed.
        :type resolved: datetime, none_type, optional

        :param severity: The incident severity.
        :type severity: IncidentSeverity, optional

        :param state: The state of the incident.
        :type state: str, none_type, optional

        :param title: The title of the incident that summarizes what happened.
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
        if created_by_uuid is not unset:
            kwargs["created_by_uuid"] = created_by_uuid
        if creation_idempotency_key is not unset:
            kwargs["creation_idempotency_key"] = creation_idempotency_key
        if customer_impact_end is not unset:
            kwargs["customer_impact_end"] = customer_impact_end
        if customer_impact_scope is not unset:
            kwargs["customer_impact_scope"] = customer_impact_scope
        if customer_impact_start is not unset:
            kwargs["customer_impact_start"] = customer_impact_start
        if declared is not unset:
            kwargs["declared"] = declared
        if declared_by_uuid is not unset:
            kwargs["declared_by_uuid"] = declared_by_uuid
        if detected is not unset:
            kwargs["detected"] = detected
        if fields is not unset:
            kwargs["fields"] = fields
        if incident_type_uuid is not unset:
            kwargs["incident_type_uuid"] = incident_type_uuid
        if is_test is not unset:
            kwargs["is_test"] = is_test
        if last_modified_by_uuid is not unset:
            kwargs["last_modified_by_uuid"] = last_modified_by_uuid
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
        if visibility is not unset:
            kwargs["visibility"] = visibility
        super().__init__(kwargs)

        self_.title = title
