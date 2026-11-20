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
    from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_type import (
        OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType,
    )


class OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_type import (
            OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(self_, auth_type: OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType, token: str, **kwargs):
        """
        Bearer token authentication. Use a project-scoped OpenAI API key with Write permission for model capabilities. While ``openai-llm-completions`` is enabled, a key that cannot call the OpenAI chat completions endpoint is rejected with a ``422`` response.

        :param auth_type: The authentication method type.
        :type auth_type: OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with OpenAI.
        :type token: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.token = token
