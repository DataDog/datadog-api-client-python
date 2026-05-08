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
    from datadog_api_client.v2.model.transport_webhook_log_email import TransportWebhookLogEmail
    from datadog_api_client.v2.model.transport_webhook_log_message import TransportWebhookLogMessage
    from datadog_api_client.v2.model.transport_webhook_log_network import TransportWebhookLogNetwork
    from datadog_api_client.v2.model.transport_webhook_log_org_metadata import TransportWebhookLogOrgMetadata


class TransportWebhookLogAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.transport_webhook_log_email import TransportWebhookLogEmail
        from datadog_api_client.v2.model.transport_webhook_log_message import TransportWebhookLogMessage
        from datadog_api_client.v2.model.transport_webhook_log_network import TransportWebhookLogNetwork
        from datadog_api_client.v2.model.transport_webhook_log_org_metadata import TransportWebhookLogOrgMetadata

        return {
            "category": ([str],),
            "email": (TransportWebhookLogEmail,),
            "email_id": (str,),
            "email_type_display_name": (str,),
            "message": (TransportWebhookLogMessage,),
            "network": (TransportWebhookLogNetwork,),
            "org": (int,),
            "org_metadata": (TransportWebhookLogOrgMetadata,),
            "org_uuid": (str,),
            "queue_time": (str,),
            "sg_machine_open": (bool,),
            "subject": (str,),
            "useragent": (str,),
        }

    attribute_map = {
        "category": "category",
        "email": "email",
        "email_id": "email_id",
        "email_type_display_name": "email_type_display_name",
        "message": "message",
        "network": "network",
        "org": "org",
        "org_metadata": "org_metadata",
        "org_uuid": "org_uuid",
        "queue_time": "queue_time",
        "sg_machine_open": "sg_machine_open",
        "subject": "subject",
        "useragent": "useragent",
    }

    def __init__(
        self_,
        category: Union[List[str], UnsetType] = unset,
        email: Union[TransportWebhookLogEmail, UnsetType] = unset,
        email_id: Union[str, UnsetType] = unset,
        email_type_display_name: Union[str, UnsetType] = unset,
        message: Union[TransportWebhookLogMessage, UnsetType] = unset,
        network: Union[TransportWebhookLogNetwork, UnsetType] = unset,
        org: Union[int, UnsetType] = unset,
        org_metadata: Union[TransportWebhookLogOrgMetadata, UnsetType] = unset,
        org_uuid: Union[str, UnsetType] = unset,
        queue_time: Union[str, UnsetType] = unset,
        sg_machine_open: Union[bool, UnsetType] = unset,
        subject: Union[str, UnsetType] = unset,
        useragent: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Top-level attributes for the webhook log event, including delivery status, recipient details, and provider metadata.

        :param category: The event categories.
        :type category: [str], optional

        :param email: The email address details.
        :type email: TransportWebhookLogEmail, optional

        :param email_id: The unique email identifier.
        :type email_id: str, optional

        :param email_type_display_name: The human-readable email type name.
        :type email_type_display_name: str, optional

        :param message: The message delivery event details.
        :type message: TransportWebhookLogMessage, optional

        :param network: The network information for the event.
        :type network: TransportWebhookLogNetwork, optional

        :param org: The numeric organization identifier.
        :type org: int, optional

        :param org_metadata: Metadata about the organization that sent the email.
        :type org_metadata: TransportWebhookLogOrgMetadata, optional

        :param org_uuid: The organization UUID.
        :type org_uuid: str, optional

        :param queue_time: The timestamp when the email was queued.
        :type queue_time: str, optional

        :param sg_machine_open: Indicates whether the open event was triggered by automated machine activity rather than a human recipient (SendGrid-specific).
        :type sg_machine_open: bool, optional

        :param subject: The email subject line.
        :type subject: str, optional

        :param useragent: The user agent string for open events.
        :type useragent: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if email is not unset:
            kwargs["email"] = email
        if email_id is not unset:
            kwargs["email_id"] = email_id
        if email_type_display_name is not unset:
            kwargs["email_type_display_name"] = email_type_display_name
        if message is not unset:
            kwargs["message"] = message
        if network is not unset:
            kwargs["network"] = network
        if org is not unset:
            kwargs["org"] = org
        if org_metadata is not unset:
            kwargs["org_metadata"] = org_metadata
        if org_uuid is not unset:
            kwargs["org_uuid"] = org_uuid
        if queue_time is not unset:
            kwargs["queue_time"] = queue_time
        if sg_machine_open is not unset:
            kwargs["sg_machine_open"] = sg_machine_open
        if subject is not unset:
            kwargs["subject"] = subject
        if useragent is not unset:
            kwargs["useragent"] = useragent
        super().__init__(kwargs)
