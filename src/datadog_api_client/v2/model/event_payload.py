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
    from datadog_api_client.v2.model.event_payload_integration_id import EventPayloadIntegrationId
    from datadog_api_client.v2.model.change_event_custom_attributes import ChangeEventCustomAttributes
    from datadog_api_client.v2.model.alert_event_custom_attributes import AlertEventCustomAttributes


class EventPayload(ModelNormal):
    validations = {
        "aggregation_key": {
            "max_length": 100,
            "min_length": 1,
        },
        "message": {
            "max_length": 4000,
            "min_length": 1,
        },
        "tags": {
            "max_items": 100,
            "min_items": 1,
        },
        "title": {
            "max_length": 500,
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_payload_attributes import EventPayloadAttributes
        from datadog_api_client.v2.model.event_category import EventCategory
        from datadog_api_client.v2.model.event_payload_integration_id import EventPayloadIntegrationId

        return {
            "aggregation_key": (str,),
            "attributes": (EventPayloadAttributes,),
            "category": (EventCategory,),
            "integration_id": (EventPayloadIntegrationId,),
            "message": (str,),
            "tags": ([str],),
            "timestamp": (str,),
            "title": (str,),
        }

    attribute_map = {
        "aggregation_key": "aggregation_key",
        "attributes": "attributes",
        "category": "category",
        "integration_id": "integration_id",
        "message": "message",
        "tags": "tags",
        "timestamp": "timestamp",
        "title": "title",
    }

    def __init__(
        self_,
        attributes: Union[EventPayloadAttributes, ChangeEventCustomAttributes, AlertEventCustomAttributes],
        category: EventCategory,
        title: str,
        aggregation_key: Union[str, UnsetType] = unset,
        integration_id: Union[EventPayloadIntegrationId, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Event attributes.

        :param aggregation_key: A string used for aggregation when `correlating <https://docs.datadoghq.com/service_management/events/correlation/>`_ events. If you specify a key, events are deduplicated to alerts based on this key. Limited to 100 characters.
        :type aggregation_key: str, optional

        :param attributes: JSON object for category-specific attributes. Schema is different per event category.
        :type attributes: EventPayloadAttributes

        :param category: Event category identifying the type of event.
        :type category: EventCategory

        :param integration_id: Integration ID sourced from integration manifests.
        :type integration_id: EventPayloadIntegrationId, optional

        :param message: Free formed text associated with the event. It's suggested to use ``data.attributes.attributes.custom`` for well-structured attributes. Limited to 4000 characters.
        :type message: str, optional

        :param tags: A list of tags associated with the event. Maximum of 100 tags allowed.
            Refer to `Tags docs <https://docs.datadoghq.com/getting_started/tagging/>`_.
        :type tags: [str], optional

        :param timestamp: Timestamp when the event occurred. Must follow `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.
            For example ``"2017-01-15T01:30:15.010000Z"``.
            Defaults to the timestamp of receipt. Limited to values no older than 18 hours.
        :type timestamp: str, optional

        :param title: The title of the event. Limited to 500 characters.
        :type title: str
        """
        if aggregation_key is not unset:
            kwargs["aggregation_key"] = aggregation_key
        if integration_id is not unset:
            kwargs["integration_id"] = integration_id
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
