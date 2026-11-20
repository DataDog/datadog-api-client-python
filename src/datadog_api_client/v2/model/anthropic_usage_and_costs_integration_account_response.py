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
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_response_data import (
        AnthropicUsageAndCostsIntegrationAccountResponseData,
    )


class AnthropicUsageAndCostsIntegrationAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_response_data import (
            AnthropicUsageAndCostsIntegrationAccountResponseData,
        )

        return {
            "data": (AnthropicUsageAndCostsIntegrationAccountResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AnthropicUsageAndCostsIntegrationAccountResponseData, **kwargs):
        """
        Response payload for a single Anthropic Usage and Costs integration account.

        :param data: Data envelope of an Anthropic Usage and Costs integration account, including server-assigned identity.
        :type data: AnthropicUsageAndCostsIntegrationAccountResponseData
        """
        super().__init__(kwargs)

        self_.data = data
