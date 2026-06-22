# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RemediationHistoryEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_type": (str,),
            "id": (str,),
            "payload": (str,),
            "timestamp_ms": (str,),
        }

    attribute_map = {
        "event_type": "event_type",
        "id": "id",
        "payload": "payload",
        "timestamp_ms": "timestamp_ms",
    }

    def __init__(
        self_,
        event_type: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        payload: Union[str, UnsetType] = unset,
        timestamp_ms: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single event in the investigation history.

        :param event_type: The type of event.
        :type event_type: str, optional

        :param id: History event ID.
        :type id: str, optional

        :param payload: Opaque JSON event body, base64-encoded. Decode and parse according to event_type.
        :type payload: str, optional

        :param timestamp_ms: Event time in epoch milliseconds (64-bit integer encoded as a string).
        :type timestamp_ms: str, optional
        """
        if event_type is not unset:
            kwargs["event_type"] = event_type
        if id is not unset:
            kwargs["id"] = id
        if payload is not unset:
            kwargs["payload"] = payload
        if timestamp_ms is not unset:
            kwargs["timestamp_ms"] = timestamp_ms
        super().__init__(kwargs)
