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


class TransportWebhookLogMessageId(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message_id": (str,),
            "smtp_id": (str,),
            "transport_event_id": (str,),
        }

    attribute_map = {
        "message_id": "message_id",
        "smtp_id": "smtp_id",
        "transport_event_id": "transport_event_id",
    }

    def __init__(
        self_,
        message_id: Union[str, UnsetType] = unset,
        smtp_id: Union[str, UnsetType] = unset,
        transport_event_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The message identifiers.

        :param message_id: The RFC 5322 Message-ID.
        :type message_id: str, optional

        :param smtp_id: The SMTP transaction identifier.
        :type smtp_id: str, optional

        :param transport_event_id: The transport provider event identifier.
        :type transport_event_id: str, optional
        """
        if message_id is not unset:
            kwargs["message_id"] = message_id
        if smtp_id is not unset:
            kwargs["smtp_id"] = smtp_id
        if transport_event_id is not unset:
            kwargs["transport_event_id"] = transport_event_id
        super().__init__(kwargs)
