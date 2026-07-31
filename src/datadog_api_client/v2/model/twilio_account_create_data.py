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
    from datadog_api_client.v2.model.twilio_account_attributes import TwilioAccountAttributes
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class TwilioAccountCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_account_attributes import TwilioAccountAttributes
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (TwilioAccountAttributes,),
            "type": (IntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TwilioAccountAttributes, type: IntegrationAccountType, **kwargs):
        """
        Data envelope for creating a Twilio integration account.

        :param attributes: Attributes of a Twilio integration account. The Twilio configuration is hoisted directly onto the attributes; there is no interface wrapper because the ``twilio`` interface is fixed by the endpoint path.
        :type attributes: TwilioAccountAttributes

        :param type: JSON:API resource type for an integration account. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
