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
    from datadog_api_client.v2.model.v2_event_attributes_attributes import V2EventAttributesAttributes
    from datadog_api_client.v2.model.change_event_attributes import ChangeEventAttributes
    from datadog_api_client.v2.model.alert_event_attributes import AlertEventAttributes


class V2EventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.v2_event_attributes_attributes import V2EventAttributesAttributes

        return {
            "attributes": (V2EventAttributesAttributes,),
            "message": (str,),
            "tags": ([str],),
            "timestamp": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "message": "message",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        attributes: Union[V2EventAttributesAttributes, ChangeEventAttributes, AlertEventAttributes, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Event attributes.

        :param attributes: JSON object for category-specific attributes.
        :type attributes: V2EventAttributesAttributes, optional

        :param message: Free-form text associated with the event.
        :type message: str, optional

        :param tags: A list of tags associated with the event.
        :type tags: [str], optional

        :param timestamp: Timestamp when the event occurred.
        :type timestamp: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if message is not unset:
            kwargs["message"] = message
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
