# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.event_alert_type import EventAlertType
    from datadog_api_client.v1.model.event_priority import EventPriority

    globals()["EventAlertType"] = EventAlertType
    globals()["EventPriority"] = EventPriority


class Event(ModelNormal):
    validations = {
        "text": {
            "max_length": 4000,
        },
    }

    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "alert_type": (EventAlertType,),
            "date_happened": (int,),
            "device_name": (str,),
            "host": (str,),
            "id": (int,),
            "id_str": (str,),
            "payload": (str,),
            "priority": (EventPriority,),
            "source_type_name": (str,),
            "tags": ([str],),
            "text": (str,),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "alert_type": "alert_type",
        "date_happened": "date_happened",
        "device_name": "device_name",
        "host": "host",
        "id": "id",
        "id_str": "id_str",
        "payload": "payload",
        "priority": "priority",
        "source_type_name": "source_type_name",
        "tags": "tags",
        "text": "text",
        "title": "title",
        "url": "url",
    }
    read_only_vars = {
        "id",
        "id_str",
        "payload",
        "url",
    }

    def __init__(self, *args, **kwargs):
        """
        Object representing an event.

        :param alert_type: If an alert event is enabled, set its type.
            For example, `error`, `warning`, `info`, `success`, `user_update`,
            `recommendation`, and `snapshot`.
        :type alert_type: EventAlertType, optional

        :param date_happened: POSIX timestamp of the event. Must be sent as an integer (that is no quotes).
            Limited to events no older than 18 hours.
        :type date_happened: int, optional

        :param device_name: A device name.
        :type device_name: str, optional

        :param host: Host name to associate with the event.
            Any tags associated with the host are also applied to this event.
        :type host: str, optional

        :param id: Integer ID of the event.
        :type id: int, optional

        :param id_str: Handling IDs as large 64-bit numbers can cause loss of accuracy issues with some programming languages.
            Instead, use the string representation of the Event ID to avoid losing accuracy.
        :type id_str: str, optional

        :param payload: Payload of the event.
        :type payload: str, optional

        :param priority: The priority of the event. For example, `normal` or `low`.
        :type priority: EventPriority, none_type, optional

        :param source_type_name: The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc.
            The list of standard source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
        :type source_type_name: str, optional

        :param tags: A list of tags to apply to the event.
        :type tags: [str], optional

        :param text: The body of the event. Limited to 4000 characters. The text supports markdown.
            To use markdown in the event text, start the text block with `%%% \n` and end the text block with `\n %%%`.
            Use `msg_text` with the Datadog Ruby library.
        :type text: str, optional

        :param title: The event title.
        :type title: str, optional

        :param url: URL of the event.
        :type url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Event, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
