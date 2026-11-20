# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_authentication_response import (
        AnthropicUsageAndCostsIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_dataflows_response import (
        AnthropicUsageAndCostsIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_bearer_token_auth_response import (
        AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthResponse,
    )


class AnthropicUsageAndCostsIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_authentication_response import (
            AnthropicUsageAndCostsIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_dataflows_response import (
            AnthropicUsageAndCostsIntegrationDataflowsResponse,
        )

        return {
            "authentication": (AnthropicUsageAndCostsIntegrationAccountAuthenticationResponse,),
            "dataflows": (AnthropicUsageAndCostsIntegrationDataflowsResponse,),
            "name": (str,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        authentication: Union[
            AnthropicUsageAndCostsIntegrationAccountAuthenticationResponse,
            AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[AnthropicUsageAndCostsIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an Anthropic Usage and Costs integration account returned in responses.

        :param authentication: Authentication configured on the Anthropic Usage and Costs integration account.
        :type authentication: AnthropicUsageAndCostsIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from Anthropic Usage and Costs, keyed by dataflow ID.
        :type dataflows: AnthropicUsageAndCostsIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Anthropic Usage and Costs integration account.
        :type name: str
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
