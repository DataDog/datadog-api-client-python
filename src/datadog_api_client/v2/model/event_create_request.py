# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
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

    def __init__(self_, attributes: EventPayload, type: EventCreateRequestType, **kwargs):
        """
        An event object.

        :param attributes: Event attributes.
        :type attributes: EventPayload

        :param type: Entity type.
        :type type: EventCreateRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
