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
    from datadog_api_client.v2.model.twilio_integration_account_create_attributes import (
        TwilioIntegrationAccountCreateAttributes,
    )
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class TwilioIntegrationAccountCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_integration_account_create_attributes import (
            TwilioIntegrationAccountCreateAttributes,
        )
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (TwilioIntegrationAccountCreateAttributes,),
            "type": (IntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TwilioIntegrationAccountCreateAttributes, type: IntegrationAccountType, **kwargs):
        """
        Data envelope for creating a Twilio integration account.

        :param attributes: Writable attributes used to create a Twilio integration account.
        :type attributes: TwilioIntegrationAccountCreateAttributes

        :param type: The type of the integration account resource. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
