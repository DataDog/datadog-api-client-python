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
    from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_type import (
        OpenAICodexIntegrationAccountBearerTokenAuthType,
    )


class OpenAICodexIntegrationAccountBearerTokenAuthUpdate(ModelNormal):
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

    def __init__(
        self_,
        auth_type: OpenAICodexIntegrationAccountBearerTokenAuthType,
        token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Bearer token authentication. Use a workspace-scoped OpenAI Admin key with the ``codex.enterprise.analytics.read`` scope. Only the fields provided are changed; omit ``token`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: OpenAICodexIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with OpenAI Codex.
        :type token: str, optional
        """
        if token is not unset:
            kwargs["token"] = token
        super().__init__(kwargs)

        self_.auth_type = auth_type
