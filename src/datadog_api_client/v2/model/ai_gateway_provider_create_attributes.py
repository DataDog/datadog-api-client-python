# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_provider_initial_binding import AiGatewayProviderInitialBinding
    from datadog_api_client.v2.model.ai_gateway_provider_integration_config import AiGatewayProviderIntegrationConfig
    from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider
    from datadog_api_client.v2.model.ai_gateway_model_input import AiGatewayModelInput


class AiGatewayProviderCreateAttributes(ModelNormal):
    validations = {
        "cost_multiplier": {
            "inclusive_maximum": 1000000,
            "exclusive_minimum": 0,
        },
        "integration_account_id": {
            "max_length": 256,
        },
        "name": {
            "max_length": 256,
            "min_length": 1,
        },
        "slug": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_initial_binding import AiGatewayProviderInitialBinding
        from datadog_api_client.v2.model.ai_gateway_provider_integration_config import (
            AiGatewayProviderIntegrationConfig,
        )
        from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider
        from datadog_api_client.v2.model.ai_gateway_model_input import AiGatewayModelInput

        return {
            "cost_multiplier": (float,),
            "initial_bindings": ([AiGatewayProviderInitialBinding],),
            "integration_account_id": (str,),
            "integration_config": (AiGatewayProviderIntegrationConfig,),
            "known_provider": (AiGatewayKnownProvider,),
            "models": ([AiGatewayModelInput],),
            "name": (str,),
            "slug": (str,),
        }

    attribute_map = {
        "cost_multiplier": "cost_multiplier",
        "initial_bindings": "initial_bindings",
        "integration_account_id": "integration_account_id",
        "integration_config": "integration_config",
        "known_provider": "known_provider",
        "models": "models",
        "name": "name",
        "slug": "slug",
    }

    def __init__(
        self_,
        name: str,
        slug: str,
        cost_multiplier: Union[float, UnsetType] = unset,
        initial_bindings: Union[List[AiGatewayProviderInitialBinding], UnsetType] = unset,
        integration_account_id: Union[str, UnsetType] = unset,
        integration_config: Union[AiGatewayProviderIntegrationConfig, UnsetType] = unset,
        known_provider: Union[AiGatewayKnownProvider, UnsetType] = unset,
        models: Union[List[AiGatewayModelInput], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to create an AI Gateway provider.

        :param cost_multiplier: Multiplier applied to provider costs. Must be greater than 0 and at most 1000000.
        :type cost_multiplier: float, optional

        :param initial_bindings: Reserved for initial View/Edit permissions. Supplying this attribute, including an empty array or null, returns HTTP 503 before discovery or persistence. Omit it for normal creation.
        :type initial_bindings: [AiGatewayProviderInitialBinding], optional

        :param integration_account_id: Provider integration account identifier.
        :type integration_account_id: str, optional

        :param integration_config: Provider-specific integration configuration.
        :type integration_config: AiGatewayProviderIntegrationConfig, optional

        :param known_provider: Known provider implementation.
        :type known_provider: AiGatewayKnownProvider, optional

        :param models: Manually managed models to add alongside models discovered from the provider integration.
        :type models: [AiGatewayModelInput], optional

        :param name: Human-readable resource name.
        :type name: str

        :param slug: Immutable routing identifier.
        :type slug: str
        """
        if cost_multiplier is not unset:
            kwargs["cost_multiplier"] = cost_multiplier
        if initial_bindings is not unset:
            kwargs["initial_bindings"] = initial_bindings
        if integration_account_id is not unset:
            kwargs["integration_account_id"] = integration_account_id
        if integration_config is not unset:
            kwargs["integration_config"] = integration_config
        if known_provider is not unset:
            kwargs["known_provider"] = known_provider
        if models is not unset:
            kwargs["models"] = models
        super().__init__(kwargs)

        self_.name = name
        self_.slug = slug
