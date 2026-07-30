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
    from datadog_api_client.v2.model.twilio_basic_auth_type import TwilioBasicAuthType


class TwilioBasicAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_basic_auth_type import TwilioBasicAuthType

        return {
            "api_key": (str,),
            "api_key_token": (str,),
            "type": (TwilioBasicAuthType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "api_key_token": "api_key_token",
        "type": "type",
    }

    def __init__(self_, api_key: str, api_key_token: str, type: TwilioBasicAuthType, **kwargs):
        """
        API Key & Secret authentication for Twilio.

        :param api_key: Twilio API Key SID for authentication. Create from Twilio Console > Account > API Keys & Tokens.
        :type api_key: str

        :param api_key_token: Twilio API Key Secret (token) corresponding to the API Key SID.
        :type api_key_token: str

        :param type: Authentication method discriminator.
        :type type: TwilioBasicAuthType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.api_key_token = api_key_token
        self_.type = type
