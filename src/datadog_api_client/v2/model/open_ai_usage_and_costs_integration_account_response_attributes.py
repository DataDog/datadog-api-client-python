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
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_authentication_response import (
        OpenAIUsageAndCostsIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_response import (
        OpenAIUsageAndCostsIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_response import (
        OpenAIUsageAndCostsIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_response import (
        OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthResponse,
    )


class OpenAIUsageAndCostsIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_authentication_response import (
            OpenAIUsageAndCostsIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_response import (
            OpenAIUsageAndCostsIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_response import (
            OpenAIUsageAndCostsIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (OpenAIUsageAndCostsIntegrationAccountAuthenticationResponse,),
            "dataflows": (OpenAIUsageAndCostsIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (OpenAIUsageAndCostsIntegrationAccountSettingsResponse,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        settings: OpenAIUsageAndCostsIntegrationAccountSettingsResponse,
        authentication: Union[
            OpenAIUsageAndCostsIntegrationAccountAuthenticationResponse,
            OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[OpenAIUsageAndCostsIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an OpenAI Usage and Costs integration account returned in responses.

        :param authentication: Authentication configured on the OpenAI Usage and Costs integration account.
        :type authentication: OpenAIUsageAndCostsIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from OpenAI Usage and Costs, keyed by dataflow ID.
        :type dataflows: OpenAIUsageAndCostsIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the OpenAI Usage and Costs integration account.
        :type name: str

        :param settings: Settings configured on the OpenAI Usage and Costs integration account.
        :type settings: OpenAIUsageAndCostsIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
