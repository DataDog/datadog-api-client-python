# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class EventResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_attributes import EventAttributes

        return {
            "attributes": (EventAttributes,),
            "tags": ([str],),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(self, *args, **kwargs):
        """
        The object description of an event response attribute.

        :param attributes: Object description of attributes from your event.
        :type attributes: EventAttributes, optional

        :param tags: An array of tags associated with the event.
        :type tags: [str], optional

        :param timestamp: The timestamp of the event.
        :type timestamp: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventResponseAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
