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


class TransportWebhookLogMessageTimestamp(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_timestamp": (float,),
            "lifetime": (float,),
            "queue_time": (float,),
            "scheduled_time": (float,),
        }

    attribute_map = {
        "event_timestamp": "event_timestamp",
        "lifetime": "lifetime",
        "queue_time": "queue_time",
        "scheduled_time": "scheduled_time",
    }

    def __init__(
        self_,
        event_timestamp: Union[float, UnsetType] = unset,
        lifetime: Union[float, UnsetType] = unset,
        queue_time: Union[float, UnsetType] = unset,
        scheduled_time: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The message delivery timing information.

        :param event_timestamp: The Unix timestamp of the event.
        :type event_timestamp: float, optional

        :param lifetime: The total delivery time in seconds.
        :type lifetime: float, optional

        :param queue_time: Number of seconds the message spent in the delivery queue.
        :type queue_time: float, optional

        :param scheduled_time: The scheduled delivery time as a Unix timestamp.
        :type scheduled_time: float, optional
        """
        if event_timestamp is not unset:
            kwargs["event_timestamp"] = event_timestamp
        if lifetime is not unset:
            kwargs["lifetime"] = lifetime
        if queue_time is not unset:
            kwargs["queue_time"] = queue_time
        if scheduled_time is not unset:
            kwargs["scheduled_time"] = scheduled_time
        super().__init__(kwargs)
