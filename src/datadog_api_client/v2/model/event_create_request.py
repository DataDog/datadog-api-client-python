# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_payload import EventPayload
    from datadog_api_client.v2.model.event_create_request_type import EventCreateRequestType


class EventCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_payload import EventPayload
        from datadog_api_client.v2.model.event_create_request_type import EventCreateRequestType

        return {
            "attributes": (EventPayload,),
            "type": (EventCreateRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[EventPayload, UnsetType] = unset,
        type: Union[EventCreateRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object representing an event creation request.

        :param attributes: Event attributes.
        :type attributes: EventPayload, optional

        :param type: Entity type.
        :type type: EventCreateRequestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
