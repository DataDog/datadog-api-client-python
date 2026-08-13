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
    from datadog_api_client.v2.model.twilio_integration_account_create_data import TwilioIntegrationAccountCreateData


class TwilioIntegrationAccountRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_integration_account_create_data import (
            TwilioIntegrationAccountCreateData,
        )

        return {
            "data": (TwilioIntegrationAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TwilioIntegrationAccountCreateData, **kwargs):
        """
        Request payload to create a Twilio integration account.

        :param data: Data envelope for creating a Twilio integration account.
        :type data: TwilioIntegrationAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
