# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class DowntimeChild(ModelNormal):
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
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.downtime_recurrence import DowntimeRecurrence

        return {
            "active": (bool,),
            "canceled": (int, none_type),
            "creator_id": (int,),
            "disabled": (bool,),
            "downtime_type": (int,),
            "end": (int, none_type),
            "id": (int,),
            "message": (str,),
            "monitor_id": (int, none_type),
            "monitor_tags": ([str],),
            "mute_first_recovery_notification": (bool,),
            "parent_id": (int, none_type),
            "recurrence": (DowntimeRecurrence,),
            "scope": ([str],),
            "start": (int,),
            "timezone": (str,),
            "updater_id": (int, none_type),
        }

    attribute_map = {
        "active": "active",
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
        "parent_id": "parent_id",
        "recurrence": "recurrence",
        "scope": "scope",
        "start": "start",
        "timezone": "timezone",
        "updater_id": "updater_id",
    }
    read_only_vars = {
        "active",
        "canceled",
        "creator_id",
        "downtime_type",
        "id",
        "updater_id",
    }

    def __init__(self, *args, **kwargs):
        """
        The downtime object definition of the active child for the original parent recurring downtime. This
        field will only exist on recurring downtimes.

        :param active: If a scheduled downtime currently exists.
        :type active: bool, optional

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
        :type message: str, optional

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

        :param parent_id: ID of the parent Downtime.
        :type parent_id: int, none_type, optional

        :param recurrence: An object defining the recurrence of the downtime.
        :type recurrence: DowntimeRecurrence, none_type, optional

        :param scope: The scope(s) to which the downtime applies. For example, ``host:app2``.
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
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DowntimeChild, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
