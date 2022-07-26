# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class EventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event import Event
        from datadog_api_client.v2.model.monitor_type import MonitorType
        from datadog_api_client.v2.model.event_priority import EventPriority
        from datadog_api_client.v2.model.event_status_type import EventStatusType

        return {
            "aggregation_key": (str,),
            "date_happened": (int,),
            "device_name": (str,),
            "duration": (int,),
            "event_object": (str,),
            "evt": (Event,),
            "hostname": (str,),
            "monitor": (MonitorType,),
            "monitor_groups": ([str], none_type),
            "monitor_id": (int, none_type),
            "priority": (EventPriority,),
            "related_event_id": (int,),
            "service": (str,),
            "source_type_name": (str,),
            "sourcecategory": (str,),
            "status": (EventStatusType,),
            "tags": ([str],),
            "timestamp": (int,),
            "title": (str,),
        }

    attribute_map = {
        "aggregation_key": "aggregation_key",
        "date_happened": "date_happened",
        "device_name": "device_name",
        "duration": "duration",
        "event_object": "event_object",
        "evt": "evt",
        "hostname": "hostname",
        "monitor": "monitor",
        "monitor_groups": "monitor_groups",
        "monitor_id": "monitor_id",
        "priority": "priority",
        "related_event_id": "related_event_id",
        "service": "service",
        "source_type_name": "source_type_name",
        "sourcecategory": "sourcecategory",
        "status": "status",
        "tags": "tags",
        "timestamp": "timestamp",
        "title": "title",
    }

    def __init__(self, *args, **kwargs):
        """
        Object description of attributes from your event.

        :param aggregation_key: Aggregation key of the event.
        :type aggregation_key: str, optional

        :param date_happened: POSIX timestamp of the event. Must be sent as an integer (no quotation marks).
            Limited to events no older than 18 hours.
        :type date_happened: int, optional

        :param device_name: A device name.
        :type device_name: str, optional

        :param duration: The duration between the triggering of the event and its recovery in nanoseconds.
        :type duration: int, optional

        :param event_object: The event title.
        :type event_object: str, optional

        :param evt: The metadata associated with a request.
        :type evt: Event, optional

        :param hostname: Host name to associate with the event.
            Any tags associated with the host are also applied to this event.
        :type hostname: str, optional

        :param monitor: Attributes from the monitor that triggered the event.
        :type monitor: MonitorType, none_type, optional

        :param monitor_groups: List of groups referred to in the event.
        :type monitor_groups: [str], none_type, optional

        :param monitor_id: ID of the monitor that triggered the event. When an event isn't related to a monitor, this field is empty.
        :type monitor_id: int, none_type, optional

        :param priority: The priority of the event's monitor. For example, ``normal`` or ``low``.
        :type priority: EventPriority, none_type, optional

        :param related_event_id: Related event ID.
        :type related_event_id: int, optional

        :param service: Service that triggered the event.
        :type service: str, optional

        :param source_type_name: The type of event being posted.
            For example, ``nagios`` , ``hudson`` , ``jenkins`` , ``my_apps`` , ``chef`` , ``puppet`` , ``git`` or ``bitbucket``.
            The list of standard source attribute values is `available here <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_.
        :type source_type_name: str, optional

        :param sourcecategory: Identifier for the source of the event, such as a monitor alert, an externally-submitted event, or an integration.
        :type sourcecategory: str, optional

        :param status: If an alert event is enabled, its status is one of the following:
            ``failure`` , ``error`` , ``warning`` , ``info`` , ``success`` , ``user_update`` ,
            ``recommendation`` , or ``snapshot``.
        :type status: EventStatusType, optional

        :param tags: A list of tags to apply to the event.
        :type tags: [str], optional

        :param timestamp: POSIX timestamp of your event in milliseconds.
        :type timestamp: int, optional

        :param title: The event title.
        :type title: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
