# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
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
    from datadog_api_client.v2.model.downtime_attribute_schedule_edit_request import (
        DowntimeAttributeScheduleEditRequest,
    )
    from datadog_api_client.v2.model.downtime_attribute_monitor_identifier_id import (
        DowntimeAttributeMonitorIdentifierId,
    )
    from datadog_api_client.v2.model.downtime_attribute_monitor_identifier_tags import (
        DowntimeAttributeMonitorIdentifierTags,
    )
    from datadog_api_client.v2.model.downtime_attribute_schedule_recurrences_edit_request import (
        DowntimeAttributeScheduleRecurrencesEditRequest,
    )
    from datadog_api_client.v2.model.downtime_attribute_schedule_one_time_create_edit_request import (
        DowntimeAttributeScheduleOneTimeCreateEditRequest,
    )


class DowntimeAttributeEditRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_attribute_monitor_identifier import DowntimeAttributeMonitorIdentifier
        from datadog_api_client.v2.model.downtime_attribute_notify_end_state_types import (
            DowntimeAttributeNotifyEndStateTypes,
        )
        from datadog_api_client.v2.model.downtime_attribute_notify_end_state_actions import (
            DowntimeAttributeNotifyEndStateActions,
        )
        from datadog_api_client.v2.model.downtime_attribute_schedule_edit_request import (
            DowntimeAttributeScheduleEditRequest,
        )

        return {
            "display_timezone": (str,),
            "message": (str,),
            "monitor_identifier": (DowntimeAttributeMonitorIdentifier,),
            "mute_first_recovery_notification": (bool,),
            "notify_end_states": ([DowntimeAttributeNotifyEndStateTypes],),
            "notify_end_types": ([DowntimeAttributeNotifyEndStateActions],),
            "schedule": (DowntimeAttributeScheduleEditRequest,),
            "scope": (str,),
        }

    attribute_map = {
        "display_timezone": "display_timezone",
        "message": "message",
        "monitor_identifier": "monitor_identifier",
        "mute_first_recovery_notification": "mute_first_recovery_notification",
        "notify_end_states": "notify_end_states",
        "notify_end_types": "notify_end_types",
        "schedule": "schedule",
        "scope": "scope",
    }

    def __init__(
        self_,
        display_timezone: Union[str, none_type, UnsetType] = unset,
        message: Union[str, none_type, UnsetType] = unset,
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
            DowntimeAttributeScheduleEditRequest,
            DowntimeAttributeScheduleRecurrencesEditRequest,
            DowntimeAttributeScheduleOneTimeCreateEditRequest,
            UnsetType,
        ] = unset,
        scope: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the downtime to update.

        :param display_timezone: The timezone in which to display the downtime's start and end times in Datadog applications. This is not used
            as an offset for scheduling.
        :type display_timezone: str, none_type, optional

        :param message: A message to include with notifications for this downtime. Email notifications can be sent to specific users
            by using the same ``@username`` notation as events.
        :type message: str, none_type, optional

        :param monitor_identifier: Monitor identifier for the downtime.
        :type monitor_identifier: DowntimeAttributeMonitorIdentifier, optional

        :param mute_first_recovery_notification: If the first recovery notification during a downtime should be muted.
        :type mute_first_recovery_notification: bool, optional

        :param notify_end_states: States that will trigger a monitor notification when the ``notify_end_types`` action occurs.
        :type notify_end_states: [DowntimeAttributeNotifyEndStateTypes], optional

        :param notify_end_types: Actions that will trigger a monitor notification if the downtime is in the ``notify_end_types`` state.
        :type notify_end_types: [DowntimeAttributeNotifyEndStateActions], optional

        :param schedule: Schedule for the downtime.
        :type schedule: DowntimeAttributeScheduleEditRequest, optional

        :param scope: The scope to which the downtime applies. Must be in
            `simple grammar syntax <https://docs.datadoghq.com/logs/explorer/search_syntax/>`_.
        :type scope: str, optional
        """
        if display_timezone is not unset:
            kwargs["display_timezone"] = display_timezone
        if message is not unset:
            kwargs["message"] = message
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
        super().__init__(kwargs)
