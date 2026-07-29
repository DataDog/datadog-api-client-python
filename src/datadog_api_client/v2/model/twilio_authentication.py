# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TwilioAuthentication(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication methods supported by the Twilio interface. Exactly one is set, selected by its ``type``.

        :param api_key: Twilio API Key SID for authentication. Create from Twilio Console > Account > API Keys & Tokens.
        :type api_key: str

        :param api_key_token: Twilio API Key Secret (token) corresponding to the API Key SID.
        :type api_key_token: str

        :param type: Authentication method discriminator.
        :type type: TwilioBasicAuthType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth

        return {
            "oneOf": [
                TwilioBasicAuth,
            ],
        }
