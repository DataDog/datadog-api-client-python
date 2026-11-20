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
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_authentication_update import (
        OpenAIUsageAndCostsIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_request import (
        OpenAIUsageAndCostsIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_update import (
        OpenAIUsageAndCostsIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_update import (
        OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthUpdate,
    )


class OpenAIUsageAndCostsIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_authentication_update import (
            OpenAIUsageAndCostsIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_request import (
            OpenAIUsageAndCostsIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_update import (
            OpenAIUsageAndCostsIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (OpenAIUsageAndCostsIntegrationAccountAuthenticationUpdate,),
            "dataflows": (OpenAIUsageAndCostsIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (OpenAIUsageAndCostsIntegrationAccountSettingsUpdate,),
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
            OpenAIUsageAndCostsIntegrationAccountAuthenticationUpdate,
            OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[OpenAIUsageAndCostsIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[OpenAIUsageAndCostsIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update an OpenAI Usage and Costs integration account. Every field is optional. Only the provided fields are changed. When ``dataflows`` is provided, only the dataflow IDs in the request are modified. Dataflows omitted from the map keep their current configuration.

        :param authentication: Authentication for updating the OpenAI Usage and Costs integration account. Exactly one method is set.
        :type authentication: OpenAIUsageAndCostsIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from OpenAI Usage and Costs, keyed by dataflow ID. Datadog always collects organization usage metrics. Each dataflow in this object adds another type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values.
        :type dataflows: OpenAIUsageAndCostsIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the OpenAI Usage and Costs integration account.
        :type name: str, optional

        :param settings: Settings for updating the OpenAI Usage and Costs integration account. Only the fields provided are changed.
        :type settings: OpenAIUsageAndCostsIntegrationAccountSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
