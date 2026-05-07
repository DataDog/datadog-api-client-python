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
    from datadog_api_client.v2.model.transport_webhook_log_message_auth import TransportWebhookLogMessageAuth
    from datadog_api_client.v2.model.transport_webhook_log_message_custom_args import (
        TransportWebhookLogMessageCustomArgs,
    )
    from datadog_api_client.v2.model.transport_webhook_log_message_id import TransportWebhookLogMessageId
    from datadog_api_client.v2.model.transport_webhook_log_message_response import TransportWebhookLogMessageResponse
    from datadog_api_client.v2.model.transport_webhook_log_message_timestamp import TransportWebhookLogMessageTimestamp


class TransportWebhookLogMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.transport_webhook_log_message_auth import TransportWebhookLogMessageAuth
        from datadog_api_client.v2.model.transport_webhook_log_message_custom_args import (
            TransportWebhookLogMessageCustomArgs,
        )
        from datadog_api_client.v2.model.transport_webhook_log_message_id import TransportWebhookLogMessageId
        from datadog_api_client.v2.model.transport_webhook_log_message_response import (
            TransportWebhookLogMessageResponse,
        )
        from datadog_api_client.v2.model.transport_webhook_log_message_timestamp import (
            TransportWebhookLogMessageTimestamp,
        )

        return {
            "auth": (TransportWebhookLogMessageAuth,),
            "custom_args": (TransportWebhookLogMessageCustomArgs,),
            "id": (TransportWebhookLogMessageId,),
            "name": (str,),
            "response": (TransportWebhookLogMessageResponse,),
            "sender_ip": (str,),
            "timestamp": (TransportWebhookLogMessageTimestamp,),
        }

    attribute_map = {
        "auth": "auth",
        "custom_args": "custom_args",
        "id": "id",
        "name": "name",
        "response": "response",
        "sender_ip": "sender_ip",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        auth: Union[TransportWebhookLogMessageAuth, UnsetType] = unset,
        custom_args: Union[TransportWebhookLogMessageCustomArgs, UnsetType] = unset,
        id: Union[TransportWebhookLogMessageId, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        response: Union[TransportWebhookLogMessageResponse, UnsetType] = unset,
        sender_ip: Union[str, UnsetType] = unset,
        timestamp: Union[TransportWebhookLogMessageTimestamp, UnsetType] = unset,
        **kwargs,
    ):
        """
        The message delivery event details.

        :param auth: The message authentication details.
        :type auth: TransportWebhookLogMessageAuth, optional

        :param custom_args: Custom arguments passed through the email transport provider for tracking.
        :type custom_args: TransportWebhookLogMessageCustomArgs, optional

        :param id: The message identifiers.
        :type id: TransportWebhookLogMessageId, optional

        :param name: The delivery event type emitted by the transport provider (for example, "delivered", "dropped", "bounced").
        :type name: str, optional

        :param response: The SMTP response information.
        :type response: TransportWebhookLogMessageResponse, optional

        :param sender_ip: The IP address of the sending server.
        :type sender_ip: str, optional

        :param timestamp: The message delivery timing information.
        :type timestamp: TransportWebhookLogMessageTimestamp, optional
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if custom_args is not unset:
            kwargs["custom_args"] = custom_args
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if response is not unset:
            kwargs["response"] = response
        if sender_ip is not unset:
            kwargs["sender_ip"] = sender_ip
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
