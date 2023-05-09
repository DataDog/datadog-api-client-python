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
    from datadog_api_client.v1.model.downtime_child import DowntimeChild
    from datadog_api_client.v1.model.notify_end_state import NotifyEndState
    from datadog_api_client.v1.model.notify_end_type import NotifyEndType
    from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence


class Downtime(ModelNormal):
    validations = {
        "creator_id": {
            "inclusive_maximum": 2147483647,
        },
        "downtime_type": {
            "inclusive_maximum": 2147483647,
        },
        "updater_id": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.downtime_child import DowntimeChild
        from datadog_api_client.v1.model.notify_end_state import NotifyEndState
        from datadog_api_client.v1.model.notify_end_type import NotifyEndType
        from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence

        return {
            "active": (bool,),
            "active_child": (DowntimeChild,),
            "canceled": (int, none_type),
            "creator_id": (int,),
            "disabled": (bool,),
            "downtime_type": (int,),
            "end": (int, none_type),
            "id": (int,),
            "message": (str, none_type),
            "monitor_id": (int, none_type),
            "monitor_tags": ([str],),
            "mute_first_recovery_notification": (bool,),
            "notify_end_states": ([NotifyEndState],),
            "notify_end_types": ([NotifyEndType],),
            "parent_id": (int, none_type),
            "recurrence": (DowntimeRecurrence,),
            "scope": ([str],),
            "start": (int,),
            "timezone": (str,),
            "updater_id": (int, none_type),
        }

    attribute_map = {
        "active": "active",
        "active_child": "active_child",
        "canceled": "canceled",
        "creator_id": "creator_id",
        "disabled": "disabled",
        "downtime_type": "downtime_type",
        "end": "end",
        "id": "id",
        "message": "message",
        "monitor_id": "monitor_id",
        "monitor_tags": "monitor_tags",
        "mute_first_recovery_notification": "mute_first_recovery_notification",
        "notify_end_states": "notify_end_states",
        "notify_end_types": "notify_end_types",
        "parent_id": "parent_id",
        "recurrence": "recurrence",
        "scope": "scope",
        "start": "start",
        "timezone": "timezone",
        "updater_id": "updater_id",
    }
    read_only_vars = {
        "active",
        "active_child",
        "canceled",
        "creator_id",
        "downtime_type",
        "id",
        "updater_id",
    }

    def __init__(
        self_,
        active: Union[bool, UnsetType] = unset,
        active_child: Union[DowntimeChild, none_type, UnsetType] = unset,
        canceled: Union[int, none_type, UnsetType] = unset,
        creator_id: Union[int, UnsetType] = unset,
        disabled: Union[bool, UnsetType] = unset,
        downtime_type: Union[int, UnsetType] = unset,
        end: Union[int, none_type, UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        message: Union[str, none_type, UnsetType] = unset,
        monitor_id: Union[int, none_type, UnsetType] = unset,
        monitor_tags: Union[List[str], UnsetType] = unset,
        mute_first_recovery_notification: Union[bool, UnsetType] = unset,
        notify_end_states: Union[List[NotifyEndState], UnsetType] = unset,
        notify_end_types: Union[List[NotifyEndType], UnsetType] = unset,
        parent_id: Union[int, none_type, UnsetType] = unset,
        recurrence: Union[DowntimeRecurrence, none_type, UnsetType] = unset,
        scope: Union[List[str], UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        updater_id: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Downtiming gives you greater control over monitor notifications by
        allowing you to globally exclude scopes from alerting.
        Downtime settings, which can be scheduled with start and end times,
        prevent all alerting related to specified Datadog tags.

        :param active: If a scheduled downtime currently exists.
        :type active: bool, optional

        :param active_child: The downtime object definition of the active child for the original parent recurring downtime. This
            field will only exist on recurring downtimes.
        :type active_child: DowntimeChild, none_type, optional

        :param canceled: If a scheduled downtime is canceled.
        :type canceled: int, none_type, optional

        :param creator_id: User ID of the downtime creator.
        :type creator_id: int, optional

        :param disabled: If a downtime has been disabled.
        :type disabled: bool, optional

        :param downtime_type: ``0`` for a downtime applied on ``*`` or all,
            ``1`` when the downtime is only scoped to hosts,
            or ``2`` when the downtime is scoped to anything but hosts.
        :type downtime_type: int, optional

        :param end: POSIX timestamp to end the downtime. If not provided,
            the downtime is in effect indefinitely until you cancel it.
        :type end: int, none_type, optional

        :param id: The downtime ID.
        :type id: int, optional

        :param message: A message to include with notifications for this downtime.
            Email notifications can be sent to specific users by using the same ``@username`` notation as events.
        :type message: str, none_type, optional

        :param monitor_id: A single monitor to which the downtime applies.
            If not provided, the downtime applies to all monitors.
        :type monitor_id: int, none_type, optional

        :param monitor_tags: A comma-separated list of monitor tags. For example, tags that are applied directly to monitors,
            not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies.
            The resulting downtime applies to monitors that match ALL provided monitor tags.
            For example, ``service:postgres`` **AND** ``team:frontend``.
        :type monitor_tags: [str], optional

        :param mute_first_recovery_notification: If the first recovery notification during a downtime should be muted.
        :type mute_first_recovery_notification: bool, optional

        :param notify_end_states: States for which ``notify_end_types`` sends out notifications for.
        :type notify_end_states: [NotifyEndState], optional

        :param notify_end_types: If set, notifies if a monitor is in an alert-worthy state ( ``ALERT`` , ``WARNING`` , or ``NO DATA`` )
            when this downtime expires or is canceled. Applied to monitors that change states during
            the downtime (such as from ``OK`` to ``ALERT`` , ``WARNING`` , or ``NO DATA`` ), and to monitors that
            already have an alert-worthy state when downtime begins.
        :type notify_end_types: [NotifyEndType], optional

        :param parent_id: ID of the parent Downtime.
        :type parent_id: int, none_type, optional

        :param recurrence: An object defining the recurrence of the downtime.
        :type recurrence: DowntimeRecurrence, none_type, optional

        :param scope: The scope(s) to which the downtime applies and must be in ``key:value`` format. For example, ``host:app2``.
            Provide multiple scopes as a comma-separated list like ``env:dev,env:prod``.
            The resulting downtime applies to sources that matches ALL provided scopes ( ``env:dev`` **AND** ``env:prod`` ).
        :type scope: [str], optional

        :param start: POSIX timestamp to start the downtime.
            If not provided, the downtime starts the moment it is created.
        :type start: int, optional

        :param timezone: The timezone in which to display the downtime's start and end times in Datadog applications.
        :type timezone: str, optional

        :param updater_id: ID of the last user that updated the downtime.
        :type updater_id: int, none_type, optional
        """
        if active is not unset:
            kwargs["active"] = active
        if active_child is not unset:
            kwargs["active_child"] = active_child
        if canceled is not unset:
            kwargs["canceled"] = canceled
        if creator_id is not unset:
            kwargs["creator_id"] = creator_id
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if downtime_type is not unset:
            kwargs["downtime_type"] = downtime_type
        if end is not unset:
            kwargs["end"] = end
        if id is not unset:
            kwargs["id"] = id
        if message is not unset:
            kwargs["message"] = message
        if monitor_id is not unset:
            kwargs["monitor_id"] = monitor_id
        if monitor_tags is not unset:
            kwargs["monitor_tags"] = monitor_tags
        if mute_first_recovery_notification is not unset:
            kwargs["mute_first_recovery_notification"] = mute_first_recovery_notification
        if notify_end_states is not unset:
            kwargs["notify_end_states"] = notify_end_states
        if notify_end_types is not unset:
            kwargs["notify_end_types"] = notify_end_types
        if parent_id is not unset:
            kwargs["parent_id"] = parent_id
        if recurrence is not unset:
            kwargs["recurrence"] = recurrence
        if scope is not unset:
            kwargs["scope"] = scope
        if start is not unset:
            kwargs["start"] = start
        if timezone is not unset:
            kwargs["timezone"] = timezone
        if updater_id is not unset:
            kwargs["updater_id"] = updater_id
        super().__init__(kwargs)
