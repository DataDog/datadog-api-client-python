# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_attributes import EventAttributes
    from datadog_api_client.v2.model.event_status_type import EventStatusType


class EventResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_attributes import EventAttributes
        from datadog_api_client.v2.model.event_status_type import EventStatusType

        return {
            "attributes": (EventAttributes,),
            "host": (str,),
            "message": (str,),
            "service": (str,),
            "status": (EventStatusType,),
            "tags": ([str],),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "host": "host",
        "message": "message",
        "service": "service",
        "status": "status",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        attributes: Union[EventAttributes, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        status: Union[EventStatusType, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object description of an event response attribute.

        :param attributes: Object description of attributes from your event.
        :type attributes: EventAttributes, optional

        :param host: The host associated with the event.
        :type host: str, optional

        :param message: The message of the event.
        :type message: str, optional

        :param service: The service associated with the event.
        :type service: str, optional

        :param status: The event status. Legacy events can use ``failure`` , ``error`` , ``warning`` ,
            ``info`` , ``success`` , ``user_update`` , ``recommendation`` , or ``snapshot``.
            Alert events can use ``error`` , ``warn`` , or ``ok``.
        :type status: EventStatusType, optional

        :param tags: An array of tags associated with the event.
        :type tags: [str], optional

        :param timestamp: The timestamp of the event.
        :type timestamp: datetime, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if host is not unset:
            kwargs["host"] = host
        if message is not unset:
            kwargs["message"] = message
        if service is not unset:
            kwargs["service"] = service
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
