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
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_authentication_request import (
        AnthropicUsageAndCostsIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_dataflows_request import (
        AnthropicUsageAndCostsIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_bearer_token_auth_request import (
        AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthRequest,
    )


class AnthropicUsageAndCostsIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_authentication_request import (
            AnthropicUsageAndCostsIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_dataflows_request import (
            AnthropicUsageAndCostsIntegrationDataflowsRequest,
        )

        return {
            "authentication": (AnthropicUsageAndCostsIntegrationAccountAuthenticationRequest,),
            "dataflows": (AnthropicUsageAndCostsIntegrationDataflowsRequest,),
            "name": (str,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
    }

    def __init__(
        self_,
        authentication: Union[
            AnthropicUsageAndCostsIntegrationAccountAuthenticationRequest,
            AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthRequest,
        ],
        name: str,
        dataflows: Union[AnthropicUsageAndCostsIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create an Anthropic Usage and Costs integration account.

        :param authentication: Authentication for creating the Anthropic Usage and Costs integration account. Exactly one method is set.
        :type authentication: AnthropicUsageAndCostsIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from Anthropic Usage and Costs, keyed by dataflow ID. Datadog always collects usage metrics. Each dataflow in this object adds another type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values. If a dataflow depends on a Datadog product, its description names that product. If you enable a dataflow without that product, Datadog stores the setting but collects no data.
        :type dataflows: AnthropicUsageAndCostsIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Anthropic Usage and Costs integration account.
        :type name: str
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
