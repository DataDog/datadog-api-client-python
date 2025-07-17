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
    from datadog_api_client.v2.model.event_system_attributes import EventSystemAttributes
    from datadog_api_client.v2.model.alert_event_attributes_links_item import AlertEventAttributesLinksItem
    from datadog_api_client.v2.model.alert_event_attributes_priority import AlertEventAttributesPriority
    from datadog_api_client.v2.model.alert_event_attributes_status import AlertEventAttributesStatus


class AlertEventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_system_attributes import EventSystemAttributes
        from datadog_api_client.v2.model.alert_event_attributes_links_item import AlertEventAttributesLinksItem
        from datadog_api_client.v2.model.alert_event_attributes_priority import AlertEventAttributesPriority
        from datadog_api_client.v2.model.alert_event_attributes_status import AlertEventAttributesStatus

        return {
            "aggregation_key": (str,),
            "custom": (dict,),
            "evt": (EventSystemAttributes,),
            "links": ([AlertEventAttributesLinksItem],),
            "priority": (AlertEventAttributesPriority,),
            "service": (str,),
            "status": (AlertEventAttributesStatus,),
            "timestamp": (int,),
            "title": (str,),
        }

    attribute_map = {
        "aggregation_key": "aggregation_key",
        "custom": "custom",
        "evt": "evt",
        "links": "links",
        "priority": "priority",
        "service": "service",
        "status": "status",
        "timestamp": "timestamp",
        "title": "title",
    }

    def __init__(
        self_,
        aggregation_key: Union[str, UnsetType] = unset,
        custom: Union[dict, UnsetType] = unset,
        evt: Union[EventSystemAttributes, UnsetType] = unset,
        links: Union[List[AlertEventAttributesLinksItem], UnsetType] = unset,
        priority: Union[AlertEventAttributesPriority, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        status: Union[AlertEventAttributesStatus, UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Alert event attributes.

        :param aggregation_key: Aggregation key of the event.
        :type aggregation_key: str, optional

        :param custom: JSON object of custom attributes.
        :type custom: dict, optional

        :param evt: JSON object of event system attributes.
        :type evt: EventSystemAttributes, optional

        :param links: The links related to the event.
        :type links: [AlertEventAttributesLinksItem], optional

        :param priority: The priority of the alert.
        :type priority: AlertEventAttributesPriority, optional

        :param service: Service that triggered the event.
        :type service: str, optional

        :param status: The status of the alert.
        :type status: AlertEventAttributesStatus, optional

        :param timestamp: POSIX timestamp of the event.
        :type timestamp: int, optional

        :param title: The title of the event.
        :type title: str, optional
        """
        if aggregation_key is not unset:
            kwargs["aggregation_key"] = aggregation_key
        if custom is not unset:
            kwargs["custom"] = custom
        if evt is not unset:
            kwargs["evt"] = evt
        if links is not unset:
            kwargs["links"] = links
        if priority is not unset:
            kwargs["priority"] = priority
        if service is not unset:
            kwargs["service"] = service
        if status is not unset:
            kwargs["status"] = status
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
