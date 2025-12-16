# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notification_channel_phone_config_type import NotificationChannelPhoneConfigType


class NotificationChannelPhoneConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_phone_config_type import (
            NotificationChannelPhoneConfigType,
        )

        return {
            "formatted_number": (str,),
            "number": (str,),
            "region": (str,),
            "sms_subscribed_at": (datetime, none_type),
            "type": (NotificationChannelPhoneConfigType,),
            "verified": (bool,),
        }

    attribute_map = {
        "formatted_number": "formatted_number",
        "number": "number",
        "region": "region",
        "sms_subscribed_at": "sms_subscribed_at",
        "type": "type",
        "verified": "verified",
    }

    def __init__(
        self_,
        formatted_number: str,
        number: str,
        region: str,
        type: NotificationChannelPhoneConfigType,
        verified: bool,
        sms_subscribed_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Phone notification channel configuration

        :param formatted_number: The formatted international version of Number (e.g. +33 7 1 23 45 67).
        :type formatted_number: str

        :param number: The E-164 formatted phone number (e.g. +3371234567)
        :type number: str

        :param region: The ISO 3166-1 alpha-2 two-letter country code.
        :type region: str

        :param sms_subscribed_at: If present, the date the user subscribed this number to SMS messages
        :type sms_subscribed_at: datetime, none_type, optional

        :param type: Indicates that the notification channel is a phone
        :type type: NotificationChannelPhoneConfigType

        :param verified: Indicates whether this phone has been verified by the user in Datadog On-Call
        :type verified: bool
        """
        if sms_subscribed_at is not unset:
            kwargs["sms_subscribed_at"] = sms_subscribed_at
        super().__init__(kwargs)

        self_.formatted_number = formatted_number
        self_.number = number
        self_.region = region
        self_.type = type
        self_.verified = verified
