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
    from datadog_api_client.v2.model.event_create_response import EventCreateResponse
    from datadog_api_client.v2.model.event_create_response_payload_links import EventCreateResponsePayloadLinks


class EventCreateResponsePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_create_response import EventCreateResponse
        from datadog_api_client.v2.model.event_create_response_payload_links import EventCreateResponsePayloadLinks

        return {
            "data": (EventCreateResponse,),
            "links": (EventCreateResponsePayloadLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(
        self_,
        data: Union[EventCreateResponse, UnsetType] = unset,
        links: Union[EventCreateResponsePayloadLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Event creation response.

        :param data: Event object.
        :type data: EventCreateResponse, optional

        :param links: Links to the event.
        :type links: EventCreateResponsePayloadLinks, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)
