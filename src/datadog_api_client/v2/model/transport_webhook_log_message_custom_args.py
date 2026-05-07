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


class TransportWebhookLogMessageCustomArgs(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email_id": (str,),
            "email_type_display_name": (str,),
            "org_uuid": (str,),
            "queue_time": (str,),
            "subject": (str,),
        }

    attribute_map = {
        "email_id": "email_id",
        "email_type_display_name": "email_type_display_name",
        "org_uuid": "org_uuid",
        "queue_time": "queue_time",
        "subject": "subject",
    }

    def __init__(
        self_,
        email_id: Union[str, UnsetType] = unset,
        email_type_display_name: Union[str, UnsetType] = unset,
        org_uuid: Union[str, UnsetType] = unset,
        queue_time: Union[str, UnsetType] = unset,
        subject: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom arguments passed through the email transport provider for tracking.

        :param email_id: The unique email identifier.
        :type email_id: str, optional

        :param email_type_display_name: The human-readable email type name.
        :type email_type_display_name: str, optional

        :param org_uuid: The organization UUID.
        :type org_uuid: str, optional

        :param queue_time: The timestamp when the email was queued.
        :type queue_time: str, optional

        :param subject: The email subject line.
        :type subject: str, optional
        """
        if email_id is not unset:
            kwargs["email_id"] = email_id
        if email_type_display_name is not unset:
            kwargs["email_type_display_name"] = email_type_display_name
        if org_uuid is not unset:
            kwargs["org_uuid"] = org_uuid
        if queue_time is not unset:
            kwargs["queue_time"] = queue_time
        if subject is not unset:
            kwargs["subject"] = subject
        super().__init__(kwargs)
