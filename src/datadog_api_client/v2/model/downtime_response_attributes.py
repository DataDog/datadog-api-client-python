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
    from datadog_api_client.v2.model.downtime_monitor_identifier import DowntimeMonitorIdentifier
    from datadog_api_client.v2.model.downtime_notify_end_state_types import DowntimeNotifyEndStateTypes
    from datadog_api_client.v2.model.downtime_notify_end_state_actions import DowntimeNotifyEndStateActions
    from datadog_api_client.v2.model.downtime_schedule_response import DowntimeScheduleResponse
    from datadog_api_client.v2.model.downtime_status import DowntimeStatus
    from datadog_api_client.v2.model.downtime_monitor_identifier_id import DowntimeMonitorIdentifierId
    from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags
    from datadog_api_client.v2.model.downtime_schedule_recurrences_response import DowntimeScheduleRecurrencesResponse
    from datadog_api_client.v2.model.downtime_schedule_one_time_response import DowntimeScheduleOneTimeResponse


class DowntimeResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_monitor_identifier import DowntimeMonitorIdentifier
        from datadog_api_client.v2.model.downtime_notify_end_state_types import DowntimeNotifyEndStateTypes
        from datadog_api_client.v2.model.downtime_notify_end_state_actions import DowntimeNotifyEndStateActions
        from datadog_api_client.v2.model.downtime_schedule_response import DowntimeScheduleResponse
        from datadog_api_client.v2.model.downtime_status import DowntimeStatus

        return {
            "canceled": (datetime, none_type),
            "created": (datetime,),
            "display_timezone": (str,),
            "message": (str,),
            "modified": (datetime,),
            "monitor_identifier": (DowntimeMonitorIdentifier,),
            "mute_first_recovery_notification": (bool,),
            "notify_end_states": ([DowntimeNotifyEndStateTypes],),
            "notify_end_types": ([DowntimeNotifyEndStateActions],),
            "schedule": (DowntimeScheduleResponse,),
            "scope": (str,),
            "status": (DowntimeStatus,),
        }

    attribute_map = {
        "canceled": "canceled",
        "created": "created",
        "display_timezone": "display_timezone",
        "message": "message",
        "modified": "modified",
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
        canceled: Union[datetime, none_type, UnsetType] = unset,
        created: Union[datetime, UnsetType] = unset,
        display_timezone: Union[str, none_type, UnsetType] = unset,
        message: Union[str, none_type, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        monitor_identifier: Union[
            DowntimeMonitorIdentifier, DowntimeMonitorIdentifierId, DowntimeMonitorIdentifierTags, UnsetType
        ] = unset,
        mute_first_recovery_notification: Union[bool, UnsetType] = unset,
        notify_end_states: Union[List[DowntimeNotifyEndStateTypes], UnsetType] = unset,
        notify_end_types: Union[List[DowntimeNotifyEndStateActions], UnsetType] = unset,
        schedule: Union[
            DowntimeScheduleResponse, DowntimeScheduleRecurrencesResponse, DowntimeScheduleOneTimeResponse, UnsetType
        ] = unset,
        scope: Union[str, UnsetType] = unset,
        status: Union[DowntimeStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Downtime details.

        :param canceled: Time that the downtime was canceled.
        :type canceled: datetime, none_type, optional

        :param created: Creation time of the downtime.
        :type created: datetime, optional

        :param display_timezone: The timezone in which to display the downtime's start and end times in Datadog applications. This is not used
            as an offset for scheduling.
        :type display_timezone: str, none_type, optional

        :param message: A message to include with notifications for this downtime. Email notifications can be sent to specific users
            by using the same ``@username`` notation as events.
        :type message: str, none_type, optional

        :param modified: Time that the downtime was last modified.
        :type modified: datetime, optional

        :param monitor_identifier: Monitor identifier for the downtime.
        :type monitor_identifier: DowntimeMonitorIdentifier, optional

        :param mute_first_recovery_notification: If the first recovery notification during a downtime should be muted.
        :type mute_first_recovery_notification: bool, optional

        :param notify_end_states: States that will trigger a monitor notification when the ``notify_end_types`` action occurs.
        :type notify_end_states: [DowntimeNotifyEndStateTypes], optional

        :param notify_end_types: Actions that will trigger a monitor notification if the downtime is in the ``notify_end_types`` state.
        :type notify_end_types: [DowntimeNotifyEndStateActions], optional

        :param schedule: The schedule that defines when the monitor starts, stops, and recurs. There are two types of schedules:
            one-time and recurring. Recurring schedules may have up to five RRULE-based recurrences. If no schedules are
            provided, the downtime will begin immediately and never end.
        :type schedule: DowntimeScheduleResponse, optional

        :param scope: The scope to which the downtime applies. Must follow the `common search syntax <https://docs.datadoghq.com/logs/explorer/search_syntax/>`_.
        :type scope: str, optional

        :param status: The current status of the downtime.
        :type status: DowntimeStatus, optional
        """
        if canceled is not unset:
            kwargs["canceled"] = canceled
        if created is not unset:
            kwargs["created"] = created
        if display_timezone is not unset:
            kwargs["display_timezone"] = display_timezone
        if message is not unset:
            kwargs["message"] = message
        if modified is not unset:
            kwargs["modified"] = modified
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
