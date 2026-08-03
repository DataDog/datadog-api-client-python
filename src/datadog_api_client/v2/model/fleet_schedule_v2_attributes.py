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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_schedule_v2_notification_rule import FleetScheduleV2NotificationRule
    from datadog_api_client.v2.model.fleet_schedule_v2_recurrence_rule import FleetScheduleV2RecurrenceRule
    from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus


class FleetScheduleV2Attributes(ModelNormal):
    validations = {
        "version_to_latest": {
            "inclusive_maximum": 2,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_v2_notification_rule import FleetScheduleV2NotificationRule
        from datadog_api_client.v2.model.fleet_schedule_v2_recurrence_rule import FleetScheduleV2RecurrenceRule
        from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus

        return {
            "created_at": (str,),
            "created_by": (str,),
            "is_default": (bool,),
            "name": (str,),
            "next_run": (str,),
            "notification_rule": (FleetScheduleV2NotificationRule,),
            "query": (str,),
            "rule": (FleetScheduleV2RecurrenceRule,),
            "status": (FleetScheduleStatus,),
            "updated_at": (str,),
            "updated_by": (str,),
            "version_to_latest": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "is_default": "is_default",
        "name": "name",
        "next_run": "next_run",
        "notification_rule": "notification_rule",
        "query": "query",
        "rule": "rule",
        "status": "status",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
        "version_to_latest": "version_to_latest",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        next_run: Union[str, UnsetType] = unset,
        notification_rule: Union[FleetScheduleV2NotificationRule, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        rule: Union[FleetScheduleV2RecurrenceRule, UnsetType] = unset,
        status: Union[FleetScheduleStatus, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        version_to_latest: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a fleet schedule in the v2 API response.

        :param created_at: RFC3339 timestamp when the schedule was created.
        :type created_at: str, optional

        :param created_by: User handle of the person who created the schedule.
        :type created_by: str, optional

        :param is_default: Whether this is the default schedule for the organization.
        :type is_default: bool, optional

        :param name: Human-readable name for the schedule.
        :type name: str, optional

        :param next_run: RFC3339 timestamp of the next scheduled maintenance window start time.
            Absent when the next run time cannot be computed.
        :type next_run: str, optional

        :param notification_rule: Notification configuration attached to a schedule.

            Included when available. If the notification rule cannot be retrieved, this field is
            omitted and the schedule is still returned. If the notification rule is retrieved but its
            handles cannot be resolved, it is still included with an empty ``handles`` array.
        :type notification_rule: FleetScheduleV2NotificationRule, optional

        :param query: Query used to filter and select target hosts for scheduled deployments.
        :type query: str, optional

        :param rule: Defines the recurrence pattern for the schedule.
        :type rule: FleetScheduleV2RecurrenceRule, optional

        :param status: The status of the schedule.

            * ``active`` : The schedule is active and will create deployments according to its recurrence rule.
            * ``inactive`` : The schedule is inactive and will not create any deployments.
        :type status: FleetScheduleStatus, optional

        :param updated_at: RFC3339 timestamp when the schedule was last updated.
        :type updated_at: str, optional

        :param updated_by: User handle of the person who last updated the schedule.
        :type updated_by: str, optional

        :param version_to_latest: Number of major versions behind the latest to target for upgrades.

            * 0: Always upgrade to the latest version.
            * 1: Upgrade to latest minus 1 major version.
            * 2: Upgrade to latest minus 2 major versions.
        :type version_to_latest: int, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if name is not unset:
            kwargs["name"] = name
        if next_run is not unset:
            kwargs["next_run"] = next_run
        if notification_rule is not unset:
            kwargs["notification_rule"] = notification_rule
        if query is not unset:
            kwargs["query"] = query
        if rule is not unset:
            kwargs["rule"] = rule
        if status is not unset:
            kwargs["status"] = status
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        if version_to_latest is not unset:
            kwargs["version_to_latest"] = version_to_latest
        super().__init__(kwargs)
