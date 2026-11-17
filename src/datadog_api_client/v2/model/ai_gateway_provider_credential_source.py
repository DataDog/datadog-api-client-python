# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayProviderCredentialSource(ModelSimple):
    """
    Whose credential the gateway sends to the provider. `integration_account` sends the integration
        account's credential. `subscription` forwards each caller's own subscription sign-in (`ChatGPT` for
        `openai`, `claude.ai` for `anthropic`) and needs no integration account.

    :param value: Must be one of ["integration_account", "subscription"].
    :type value: str
    """

    allowed_values = {
        "integration_account",
        "subscription",
    }
    INTEGRATION_ACCOUNT: ClassVar["AiGatewayProviderCredentialSource"]
    SUBSCRIPTION: ClassVar["AiGatewayProviderCredentialSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayProviderCredentialSource.INTEGRATION_ACCOUNT = AiGatewayProviderCredentialSource("integration_account")
AiGatewayProviderCredentialSource.SUBSCRIPTION = AiGatewayProviderCredentialSource("subscription")
