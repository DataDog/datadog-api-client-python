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
    from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_type import (
        OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType,
    )


class OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_type import (
            OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(
        self_,
        auth_type: OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType,
        token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Bearer token authentication. Use an admin-scoped OpenAI API key; project-scoped and standard keys cannot read organization usage or costs. A key that is not an admin key, or that is invalid, is rejected with a ``422`` response. Only the provided fields are changed. To keep the stored token, omit ``token``.

        :param auth_type: The authentication method type.
        :type auth_type: OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with OpenAI.
        :type token: str, optional
        """
        if token is not unset:
            kwargs["token"] = token
        super().__init__(kwargs)

        self_.auth_type = auth_type
