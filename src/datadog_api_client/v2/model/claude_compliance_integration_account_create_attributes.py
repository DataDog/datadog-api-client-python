# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.claude_compliance_integration_account_authentication_request import (
        ClaudeComplianceIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_request import (
        ClaudeComplianceIntegrationAccountBearerTokenAuthRequest,
    )


class ClaudeComplianceIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_integration_account_authentication_request import (
            ClaudeComplianceIntegrationAccountAuthenticationRequest,
        )

        return {
            "authentication": (ClaudeComplianceIntegrationAccountAuthenticationRequest,),
            "name": (str,),
        }

    attribute_map = {
        "authentication": "authentication",
        "name": "name",
    }

    def __init__(
        self_,
        authentication: Union[
            ClaudeComplianceIntegrationAccountAuthenticationRequest,
            ClaudeComplianceIntegrationAccountBearerTokenAuthRequest,
        ],
        name: str,
        **kwargs,
    ):
        """
        Writable attributes used to create a Claude Compliance integration account.

        :param authentication: Authentication for creating the Claude Compliance integration account. Exactly one method is set.
        :type authentication: ClaudeComplianceIntegrationAccountAuthenticationRequest

        :param name: Human-readable name of the Claude Compliance integration account.
        :type name: str
        """
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
