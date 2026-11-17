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
    from datadog_api_client.v2.model.ai_gateway_provider_credential_source import AiGatewayProviderCredentialSource
    from datadog_api_client.v2.model.ai_gateway_provider_integration_config import AiGatewayProviderIntegrationConfig
    from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider
    from datadog_api_client.v2.model.ai_gateway_provider_status import AiGatewayProviderStatus


class AiGatewayProviderAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_credential_source import AiGatewayProviderCredentialSource
        from datadog_api_client.v2.model.ai_gateway_provider_integration_config import (
            AiGatewayProviderIntegrationConfig,
        )
        from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider
        from datadog_api_client.v2.model.ai_gateway_provider_status import AiGatewayProviderStatus

        return {
            "cost_multiplier": (float,),
            "created_at": (datetime,),
            "credential_source": (AiGatewayProviderCredentialSource,),
            "integration_account_id": (str,),
            "integration_config": (AiGatewayProviderIntegrationConfig,),
            "known_provider": (AiGatewayKnownProvider,),
            "name": (str,),
            "slug": (str,),
            "status": (AiGatewayProviderStatus,),
            "updated_at": (datetime,),
            "zdr_eligible": (bool,),
        }

    attribute_map = {
        "cost_multiplier": "cost_multiplier",
        "created_at": "created_at",
        "credential_source": "credential_source",
        "integration_account_id": "integration_account_id",
        "integration_config": "integration_config",
        "known_provider": "known_provider",
        "name": "name",
        "slug": "slug",
        "status": "status",
        "updated_at": "updated_at",
        "zdr_eligible": "zdr_eligible",
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
        credential_source: Union[AiGatewayProviderCredentialSource, UnsetType] = unset,
        integration_config: Union[AiGatewayProviderIntegrationConfig, UnsetType] = unset,
        status: Union[AiGatewayProviderStatus, UnsetType] = unset,
        zdr_eligible: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        AI Gateway provider configuration and metadata.

        :param cost_multiplier: Multiplier applied to provider costs.
        :type cost_multiplier: float

        :param created_at: Time when the resource was created.
        :type created_at: datetime

        :param credential_source: Whose credential the gateway sends to the provider. ``integration_account`` sends the integration
            account's credential. ``subscription`` forwards each caller's own subscription sign-in ( ``ChatGPT`` for
            ``openai`` , ``claude.ai`` for ``anthropic`` ) and needs no integration account.
        :type credential_source: AiGatewayProviderCredentialSource, optional

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

        :param status: Read-only. Whether the provider is working, based on the model sync and live calls. Omitted for
            providers that are never checked, which include providers without an integration account, and
            Azure OpenAI and Gemini providers until live traffic records a status.
        :type status: AiGatewayProviderStatus, optional

        :param updated_at: Time when the resource was last updated.
        :type updated_at: datetime

        :param zdr_eligible: Whether this provider connection is covered by a zero data retention agreement.
        :type zdr_eligible: bool, optional
        """
        if credential_source is not unset:
            kwargs["credential_source"] = credential_source
        if integration_config is not unset:
            kwargs["integration_config"] = integration_config
        if status is not unset:
            kwargs["status"] = status
        if zdr_eligible is not unset:
            kwargs["zdr_eligible"] = zdr_eligible
        super().__init__(kwargs)

        self_.cost_multiplier = cost_multiplier
        self_.created_at = created_at
        self_.integration_account_id = integration_account_id
        self_.known_provider = known_provider
        self_.name = name
        self_.slug = slug
        self_.updated_at = updated_at
