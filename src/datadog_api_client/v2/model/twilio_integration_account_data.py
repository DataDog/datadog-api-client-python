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
    from datadog_api_client.v2.model.twilio_integration_account_attributes import TwilioIntegrationAccountAttributes
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class TwilioIntegrationAccountData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_integration_account_attributes import TwilioIntegrationAccountAttributes
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (TwilioIntegrationAccountAttributes,),
            "id": (str,),
            "type": (IntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_, attributes: TwilioIntegrationAccountAttributes, id: str, type: IntegrationAccountType, **kwargs
    ):
        """
        Data envelope of a Twilio integration account, including server-assigned identity.

        :param attributes: Attributes of a Twilio integration account.
        :type attributes: TwilioIntegrationAccountAttributes

        :param id: Server-generated unique identifier of the integration account.
        :type id: str

        :param type: JSON:API resource type for an integration account. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
