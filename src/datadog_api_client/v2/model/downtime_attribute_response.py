# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.downtime_attribute_monitor_identifier import DowntimeAttributeMonitorIdentifier
    from datadog_api_client.v2.model.downtime_attribute_notify_end_state_types import (
        DowntimeAttributeNotifyEndStateTypes,
    )
    from datadog_api_client.v2.model.downtime_attribute_notify_end_state_actions import (
        DowntimeAttributeNotifyEndStateActions,
    )
    from datadog_api_client.v2.model.downtime_attribute_schedule_response import DowntimeAttributeScheduleResponse
    from datadog_api_client.v2.model.downtime_status_enum import DowntimeStatusEnum
    from datadog_api_client.v2.model.downtime_attribute_monitor_identifier_id import (
        DowntimeAttributeMonitorIdentifierId,
    )
    from datadog_api_client.v2.model.downtime_attribute_monitor_identifier_tags import (
        DowntimeAttributeMonitorIdentifierTags,
    )
    from datadog_api_client.v2.model.downtime_attribute_schedule_recurrences_response import (
        DowntimeAttributeScheduleRecurrencesResponse,
    )
    from datadog_api_client.v2.model.downtime_attribute_schedule_one_time_response import (
        DowntimeAttributeScheduleOneTimeResponse,
    )


class DowntimeAttributeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_attribute_monitor_identifier import DowntimeAttributeMonitorIdentifier
        from datadog_api_client.v2.model.downtime_attribute_notify_end_state_types import (
            DowntimeAttributeNotifyEndStateTypes,
        )
        from datadog_api_client.v2.model.downtime_attribute_notify_end_state_actions import (
            DowntimeAttributeNotifyEndStateActions,
        )
        from datadog_api_client.v2.model.downtime_attribute_schedule_response import DowntimeAttributeScheduleResponse
        from datadog_api_client.v2.model.downtime_status_enum import DowntimeStatusEnum

        return {
            "created_at": (datetime,),
            "display_timezone": (str,),
            "message": (str,),
            "modified_at": (datetime,),
            "monitor_identifier": (DowntimeAttributeMonitorIdentifier,),
            "mute_first_recovery_notification": (bool,),
            "notify_end_states": ([DowntimeAttributeNotifyEndStateTypes],),
            "notify_end_types": ([DowntimeAttributeNotifyEndStateActions],),
            "schedule": (DowntimeAttributeScheduleResponse,),
            "scope": (str,),
            "status": (DowntimeStatusEnum,),
        }

    attribute_map = {
        "created_at": "created_at",
        "display_timezone": "display_timezone",
        "message": "message",
        "modified_at": "modified_at",
        "monitor_identifier": "monitor_identifier",
        "mute_first_recovery_notification": "mute_first_recovery_notification",
        "notify_end_states": "notify_end_states",
        "notify_end_types": "notify_end_types",
        "schedule": "schedule",
        "scope": "scope",
        "status": "status",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        display_timezone: Union[str, none_type, UnsetType] = unset,
        message: Union[str, none_type, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        monitor_identifier: Union[
            DowntimeAttributeMonitorIdentifier,
            DowntimeAttributeMonitorIdentifierId,
            DowntimeAttributeMonitorIdentifierTags,
            UnsetType,
        ] = unset,
        mute_first_recovery_notification: Union[bool, UnsetType] = unset,
        notify_end_states: Union[List[DowntimeAttributeNotifyEndStateTypes], UnsetType] = unset,
        notify_end_types: Union[List[DowntimeAttributeNotifyEndStateActions], UnsetType] = unset,
        schedule: Union[
            DowntimeAttributeScheduleResponse,
            DowntimeAttributeScheduleRecurrencesResponse,
            DowntimeAttributeScheduleOneTimeResponse,
            UnsetType,
        ] = unset,
        scope: Union[str, UnsetType] = unset,
        status: Union[DowntimeStatusEnum, UnsetType] = unset,
        **kwargs,
    ):
        """
        Downtime details.

        :param created_at: Creation time of the downtime.
        :type created_at: datetime, optional

        :param display_timezone: The timezone in which to display the downtime's start and end times in Datadog applications. This is not used
            as an offset for scheduling.
        :type display_timezone: str, none_type, optional

        :param message: A message to include with notifications for this downtime. Email notifications can be sent to specific users
            by using the same ``@username`` notation as events.
        :type message: str, none_type, optional

        :param modified_at: Time that the downtime was last modified.
        :type modified_at: datetime, optional

        :param monitor_identifier: Monitor identifier for the downtime.
        :type monitor_identifier: DowntimeAttributeMonitorIdentifier, optional

        :param mute_first_recovery_notification: If the first recovery notification during a downtime should be muted.
        :type mute_first_recovery_notification: bool, optional

        :param notify_end_states: States that will trigger a monitor notification when the ``notify_end_types`` action occurs.
        :type notify_end_states: [DowntimeAttributeNotifyEndStateTypes], optional

        :param notify_end_types: Actions that will trigger a monitor notification if the downtime is in the ``notify_end_types`` state.
        :type notify_end_types: [DowntimeAttributeNotifyEndStateActions], optional

        :param schedule: The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules:
            one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules is
            provided, the downtime will begin immediately and never end.
        :type schedule: DowntimeAttributeScheduleResponse, optional

        :param scope: The scope to which the downtime applies. Must be in
            `simple grammar syntax <https://docs.datadoghq.com/logs/explorer/search_syntax/>`_.
        :type scope: str, optional

        :param status: The current status of the downtime.
        :type status: DowntimeStatusEnum, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if display_timezone is not unset:
            kwargs["display_timezone"] = display_timezone
        if message is not unset:
            kwargs["message"] = message
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if monitor_identifier is not unset:
            kwargs["monitor_identifier"] = monitor_identifier
        if mute_first_recovery_notification is not unset:
            kwargs["mute_first_recovery_notification"] = mute_first_recovery_notification
        if notify_end_states is not unset:
            kwargs["notify_end_states"] = notify_end_states
        if notify_end_types is not unset:
            kwargs["notify_end_types"] = notify_end_types
        if schedule is not unset:
            kwargs["schedule"] = schedule
        if scope is not unset:
            kwargs["scope"] = scope
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
