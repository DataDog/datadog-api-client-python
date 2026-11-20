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
    from datadog_api_client.v2.model.claude_compliance_integration_account_authentication_update import (
        ClaudeComplianceIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_update import (
        ClaudeComplianceIntegrationAccountBearerTokenAuthUpdate,
    )


class ClaudeComplianceIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_integration_account_authentication_update import (
            ClaudeComplianceIntegrationAccountAuthenticationUpdate,
        )

        return {
            "authentication": (ClaudeComplianceIntegrationAccountAuthenticationUpdate,),
            "name": (str,),
        }

    attribute_map = {
        "authentication": "authentication",
        "name": "name",
    }

    def __init__(
        self_,
        authentication: Union[
            ClaudeComplianceIntegrationAccountAuthenticationUpdate,
            ClaudeComplianceIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a Claude Compliance integration account. Every field is optional. Only the provided fields are changed.

        :param authentication: Authentication for updating the Claude Compliance integration account. Exactly one method is set.
        :type authentication: ClaudeComplianceIntegrationAccountAuthenticationUpdate, optional

        :param name: Human-readable name of the Claude Compliance integration account.
        :type name: str, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
