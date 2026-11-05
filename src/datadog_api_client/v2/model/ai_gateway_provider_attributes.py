# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_provider_integration_config import AiGatewayProviderIntegrationConfig
    from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider


class AiGatewayProviderAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_integration_config import (
            AiGatewayProviderIntegrationConfig,
        )
        from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider

        return {
            "cost_multiplier": (float,),
            "created_at": (datetime,),
            "integration_account_id": (str,),
            "integration_config": (AiGatewayProviderIntegrationConfig,),
            "known_provider": (AiGatewayKnownProvider,),
            "name": (str,),
            "slug": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "cost_multiplier": "cost_multiplier",
        "created_at": "created_at",
        "integration_account_id": "integration_account_id",
        "integration_config": "integration_config",
        "known_provider": "known_provider",
        "name": "name",
        "slug": "slug",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        cost_multiplier: float,
        created_at: datetime,
        integration_account_id: str,
        known_provider: AiGatewayKnownProvider,
        name: str,
        slug: str,
        updated_at: datetime,
        integration_config: Union[AiGatewayProviderIntegrationConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        AI Gateway provider configuration and metadata.

        :param cost_multiplier: Multiplier applied to provider costs.
        :type cost_multiplier: float

        :param created_at: Time when the resource was created.
        :type created_at: datetime

        :param integration_account_id: Provider integration account identifier.
        :type integration_account_id: str

        :param integration_config: Provider-specific integration configuration.
        :type integration_config: AiGatewayProviderIntegrationConfig, optional

        :param known_provider: Known provider implementation.
        :type known_provider: AiGatewayKnownProvider

        :param name: Human-readable resource name.
        :type name: str

        :param slug: Immutable routing identifier.
        :type slug: str

        :param updated_at: Time when the resource was last updated.
        :type updated_at: datetime
        """
        if integration_config is not unset:
            kwargs["integration_config"] = integration_config
        super().__init__(kwargs)

        self_.cost_multiplier = cost_multiplier
        self_.created_at = created_at
        self_.integration_account_id = integration_account_id
        self_.known_provider = known_provider
        self_.name = name
        self_.slug = slug
        self_.updated_at = updated_at
