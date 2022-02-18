# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.event import Event

    globals()["Event"] = Event


class EventCreateResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "event": (Event,),
            "status": (str,),
        }

    attribute_map = {
        "event": "event",
        "status": "status",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object containing an event response.

<<<<<<< HEAD
        :type event: Event, optional

        :param status: A status.
        :type status: str, optional
=======
        :param alert_type: If an alert event is enabled, set its type.
            For example, `error`, `warning`, `info`, `success`, `user_update`,
            `recommendation`, and `snapshot`.
        :type alert_type: EventAlertType, optional

        :param date_happened: POSIX timestamp of the event. Must be sent as an integer (that is no quotes).
            Limited to events no older than 7 days.
        :type date_happened: int, optional

        :param device_name: A device name.
        :type device_name: str, optional

        :param host: Host name to associate with the event.
            Any tags associated with the host are also applied to this event.
        :type host: str, optional

        :param id: Integer ID of the event.
        :type id: int, optional

        :param payload: Payload of the event.
        :type payload: str, optional

        :param priority: The priority of the event. For example, `normal` or `low`.
        :type priority: EventPriority, optional

        :param related_event_id: ID of the parent event. Must be sent as an integer (that is no quotes).
        :type related_event_id: int, optional

        :param source_type_name: The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc.
            A complete list of source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
        :type source_type_name: str, optional

        :param status: A status.
        :type status: str, optional

        :param tags: A list of tags to apply to the event.
        :type tags: [str], optional

        :param text: The body of the event. Limited to 4000 characters. The text supports markdown.
            Use `msg_text` with the Datadog Ruby library.
        :type text: str, optional

        :param title: The event title. Limited to 100 characters. Use `msg_title` with the Datadog Ruby library.
        :type title: str, optional

        :param url: URL of the event.
        :type url: str, optional
>>>>>>> 39b80a488 (Use new generator for Python)
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventCreateResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
