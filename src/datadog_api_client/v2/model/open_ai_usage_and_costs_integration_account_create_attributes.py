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
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_authentication_request import (
        OpenAIUsageAndCostsIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_request import (
        OpenAIUsageAndCostsIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_request import (
        OpenAIUsageAndCostsIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_request import (
        OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthRequest,
    )


class OpenAIUsageAndCostsIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_authentication_request import (
            OpenAIUsageAndCostsIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_request import (
            OpenAIUsageAndCostsIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_request import (
            OpenAIUsageAndCostsIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (OpenAIUsageAndCostsIntegrationAccountAuthenticationRequest,),
            "dataflows": (OpenAIUsageAndCostsIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (OpenAIUsageAndCostsIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            OpenAIUsageAndCostsIntegrationAccountAuthenticationRequest,
            OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthRequest,
        ],
        name: str,
        settings: OpenAIUsageAndCostsIntegrationAccountSettingsRequest,
        dataflows: Union[OpenAIUsageAndCostsIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create an OpenAI Usage and Costs integration account.

        :param authentication: Authentication for creating the OpenAI Usage and Costs integration account. Set exactly one method.
        :type authentication: OpenAIUsageAndCostsIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from OpenAI Usage and Costs, keyed by dataflow ID. Datadog always collects organization usage metrics. Each dataflow in this object adds another type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values.
        :type dataflows: OpenAIUsageAndCostsIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the OpenAI Usage and Costs integration account.
        :type name: str

        :param settings: Settings for creating the OpenAI Usage and Costs integration account.
        :type settings: OpenAIUsageAndCostsIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
