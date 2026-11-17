# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayProviderCreateCredentialSource(ModelSimple):
    """
    Whose credential the gateway sends to the provider. Defaults to `integration_account`, which sends
        the integration account's credential. `subscription` forwards each caller's own subscription sign-in
        (`ChatGPT` for `openai`, `claude.ai` for `anthropic`) and needs no integration account; it is available
        only to organizations with subscription providers enabled. A subscription provider's models are
        optional: callers can use any model their subscription includes, and a model you add sets its
        pricing. Immutable.

    :param value: If omitted defaults to "integration_account". Must be one of ["integration_account", "subscription"].
    :type value: str
    """

    allowed_values = {
        "integration_account",
        "subscription",
    }
    INTEGRATION_ACCOUNT: ClassVar["AiGatewayProviderCreateCredentialSource"]
    SUBSCRIPTION: ClassVar["AiGatewayProviderCreateCredentialSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayProviderCreateCredentialSource.INTEGRATION_ACCOUNT = AiGatewayProviderCreateCredentialSource(
    "integration_account"
)
AiGatewayProviderCreateCredentialSource.SUBSCRIPTION = AiGatewayProviderCreateCredentialSource("subscription")
