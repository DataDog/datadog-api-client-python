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
    from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_type import (
        ClaudeComplianceIntegrationAccountBearerTokenAuthType,
    )


class ClaudeComplianceIntegrationAccountBearerTokenAuthRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_type import (
            ClaudeComplianceIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (ClaudeComplianceIntegrationAccountBearerTokenAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(self_, auth_type: ClaudeComplianceIntegrationAccountBearerTokenAuthType, token: str, **kwargs):
        """
        Bearer token authentication. Use an Anthropic Admin API key with the ``read:compliance_activities`` scope, or a dedicated Compliance Access key.

        :param auth_type: The authentication method type.
        :type auth_type: ClaudeComplianceIntegrationAccountBearerTokenAuthType

        :param token: Anthropic Admin API key (prefix ``sk-ant-admin01-`` ) with the ``read:compliance_activities`` scope, or a dedicated Compliance Access key (prefix ``sk-ant-api01-`` ). Generate an Admin API key in the Anthropic Console under **Organization settings > API keys**.
        :type token: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.token = token
