# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_payload_attributes import EventPayloadAttributes
    from datadog_api_client.v2.model.event_category import EventCategory
    from datadog_api_client.v2.model.change_event_custom_attributes import ChangeEventCustomAttributes


class EventPayload(ModelNormal):
    validations = {
        "aggregation_key": {
            "max_length": 100,
        },
        "message": {
            "max_length": 4000,
        },
        "title": {
            "max_length": 500,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_payload_attributes import EventPayloadAttributes
        from datadog_api_client.v2.model.event_category import EventCategory

        return {
            "aggregation_key": (str,),
            "attributes": (EventPayloadAttributes,),
            "category": (EventCategory,),
            "message": (str,),
            "tags": ([str],),
            "timestamp": (str,),
            "title": (str,),
        }

    attribute_map = {
        "aggregation_key": "aggregation_key",
        "attributes": "attributes",
        "category": "category",
        "message": "message",
        "tags": "tags",
        "timestamp": "timestamp",
        "title": "title",
    }

    def __init__(
        self_,
        attributes: Union[EventPayloadAttributes, ChangeEventCustomAttributes],
        category: EventCategory,
        title: str,
        aggregation_key: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Event attributes.

        :param aggregation_key: An arbitrary string to use for aggregation when correlating events. Limited to 100 characters.
        :type aggregation_key: str, optional

        :param attributes: JSON object for custom attributes. Schema are different per each event category.
        :type attributes: EventPayloadAttributes

        :param category: Event category to identify the type of event. Only the value ``change`` is supported. Support for other categories are coming. please reach out to datadog support if you're interested.
        :type category: EventCategory

        :param message: The body of the event. Limited to 4000 characters.
        :type message: str, optional

        :param tags: A list of tags to apply to the event.
            Refer to `Tags docs <https://docs.datadoghq.com/getting_started/tagging/>`_.
        :type tags: [str], optional

        :param timestamp: Timestamp when the event occurred. Must follow `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.
            For example ``"2017-01-15T01:30:15.010000Z"``.
            Defaults to the timestamp of receipt. Limited to values no older than 18 hours.
        :type timestamp: str, optional

        :param title: The event title. Limited to 500 characters.
        :type title: str
        """
        if aggregation_key is not unset:
            kwargs["aggregation_key"] = aggregation_key
        if message is not unset:
            kwargs["message"] = message
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.category = category
        self_.title = title
