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
    from datadog_api_client.v2.model.fleet_schedule_recurrence_rule import FleetScheduleRecurrenceRule
    from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus


class FleetScheduleAttributes(ModelNormal):
    validations = {
        "version_to_latest": {
            "inclusive_maximum": 2,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_schedule_recurrence_rule import FleetScheduleRecurrenceRule
        from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus

        return {
            "created_at_unix": (int,),
            "created_by": (str,),
            "name": (str,),
            "query": (str,),
            "rule": (FleetScheduleRecurrenceRule,),
            "status": (FleetScheduleStatus,),
            "updated_at_unix": (int,),
            "updated_by": (str,),
            "version_to_latest": (int,),
        }

    attribute_map = {
        "created_at_unix": "created_at_unix",
        "created_by": "created_by",
        "name": "name",
        "query": "query",
        "rule": "rule",
        "status": "status",
        "updated_at_unix": "updated_at_unix",
        "updated_by": "updated_by",
        "version_to_latest": "version_to_latest",
    }

    def __init__(
        self_,
        created_at_unix: Union[int, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        rule: Union[FleetScheduleRecurrenceRule, UnsetType] = unset,
        status: Union[FleetScheduleStatus, UnsetType] = unset,
        updated_at_unix: Union[int, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        version_to_latest: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a schedule in the response.

        :param created_at_unix: Unix timestamp (seconds since epoch) when the schedule was created.
        :type created_at_unix: int, optional

        :param created_by: User handle of the person who created the schedule.
        :type created_by: str, optional

        :param name: Human-readable name for the schedule.
        :type name: str, optional

        :param query: Query used to filter and select target hosts for scheduled deployments. Uses the Datadog query syntax.
        :type query: str, optional

        :param rule: Defines the recurrence pattern for the schedule. Specifies when deployments should be
            automatically triggered based on maintenance windows.
        :type rule: FleetScheduleRecurrenceRule, optional

        :param status: The status of the schedule.

            * ``active`` : The schedule is active and will create deployments according to its recurrence rule.
            * ``inactive`` : The schedule is inactive and will not create any deployments.
        :type status: FleetScheduleStatus, optional

        :param updated_at_unix: Unix timestamp (seconds since epoch) when the schedule was last updated.
        :type updated_at_unix: int, optional

        :param updated_by: User handle of the person who last updated the schedule.
        :type updated_by: str, optional

        :param version_to_latest: Number of major versions behind the latest to target for upgrades.

            * 0: Always upgrade to the latest version
            * 1: Upgrade to latest minus 1 major version
            * 2: Upgrade to latest minus 2 major versions
              Maximum value is 2.
        :type version_to_latest: int, optional
        """
        if created_at_unix is not unset:
            kwargs["created_at_unix"] = created_at_unix
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        if rule is not unset:
            kwargs["rule"] = rule
        if status is not unset:
            kwargs["status"] = status
        if updated_at_unix is not unset:
            kwargs["updated_at_unix"] = updated_at_unix
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        if version_to_latest is not unset:
            kwargs["version_to_latest"] = version_to_latest
        super().__init__(kwargs)
