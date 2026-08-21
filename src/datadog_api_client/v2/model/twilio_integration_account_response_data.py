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
    from datadog_api_client.v2.model.twilio_integration_account_response_attributes import (
        TwilioIntegrationAccountResponseAttributes,
    )
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class TwilioIntegrationAccountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_integration_account_response_attributes import (
            TwilioIntegrationAccountResponseAttributes,
        )
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (TwilioIntegrationAccountResponseAttributes,),
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
        self_, attributes: TwilioIntegrationAccountResponseAttributes, id: str, type: IntegrationAccountType, **kwargs
    ):
        """
        Data envelope of a Twilio integration account, including server-assigned identity.

        :param attributes: Attributes of a Twilio integration account returned in responses.
        :type attributes: TwilioIntegrationAccountResponseAttributes

        :param id: Server-generated unique identifier of the Twilio integration account.
        :type id: str

        :param type: The type of the integration account resource. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
