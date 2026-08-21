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


class TwilioIntegrationAccountSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_sid": (str,),
            "censor_logs": (bool,),
        }

    attribute_map = {
        "account_sid": "account_sid",
        "censor_logs": "censor_logs",
    }

    def __init__(self_, account_sid: str, censor_logs: Union[bool, UnsetType] = unset, **kwargs):
        """
        Settings configured on the Twilio integration account.

        :param account_sid: Twilio Account SID that uniquely identifies your Twilio account.
        :type account_sid: str

        :param censor_logs: When enabled, Twilio phone numbers in the ``to`` field and SMS message bodies are censored for privacy.
        :type censor_logs: bool, optional
        """
        if censor_logs is not unset:
            kwargs["censor_logs"] = censor_logs
        super().__init__(kwargs)

        self_.account_sid = account_sid
