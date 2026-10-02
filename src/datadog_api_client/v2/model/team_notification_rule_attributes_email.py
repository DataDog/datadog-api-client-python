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


class TeamNotificationRuleAttributesEmail(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "recipient_email": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "recipient_email": "recipient_email",
    }

    def __init__(
        self_, enabled: Union[bool, UnsetType] = unset, recipient_email: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Email notification settings for the team

        :param enabled: Flag indicating email notification
        :type enabled: bool, optional

        :param recipient_email: Email address to notify. When omitted and email notifications are enabled, notifications are sent to all team members.
        :type recipient_email: str, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if recipient_email is not unset:
            kwargs["recipient_email"] = recipient_email
        super().__init__(kwargs)
