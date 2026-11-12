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
    from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_type import (
        OpenAICodexIntegrationAccountBearerTokenAuthType,
    )


class OpenAICodexIntegrationAccountBearerTokenAuthRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_type import (
            OpenAICodexIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (OpenAICodexIntegrationAccountBearerTokenAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(self_, auth_type: OpenAICodexIntegrationAccountBearerTokenAuthType, token: str, **kwargs):
        """
        Bearer token authentication. Use a workspace-scoped OpenAI Admin key with the ``codex.enterprise.analytics.read`` scope.

        :param auth_type: The authentication method type.
        :type auth_type: OpenAICodexIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with OpenAI Codex.
        :type token: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.token = token
