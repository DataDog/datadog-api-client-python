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
    from datadog_api_client.v2.model.claude_compliance_integration_account_authentication_response import (
        ClaudeComplianceIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.claude_compliance_integration_dataflows_response import (
        ClaudeComplianceIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_response import (
        ClaudeComplianceIntegrationAccountBearerTokenAuthResponse,
    )


class ClaudeComplianceIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_integration_account_authentication_response import (
            ClaudeComplianceIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.claude_compliance_integration_dataflows_response import (
            ClaudeComplianceIntegrationDataflowsResponse,
        )

        return {
            "authentication": (ClaudeComplianceIntegrationAccountAuthenticationResponse,),
            "dataflows": (ClaudeComplianceIntegrationDataflowsResponse,),
            "name": (str,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        authentication: Union[
            ClaudeComplianceIntegrationAccountAuthenticationResponse,
            ClaudeComplianceIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[ClaudeComplianceIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Claude Compliance integration account returned in responses.

        :param authentication: Authentication configured on the Claude Compliance integration account.
        :type authentication: ClaudeComplianceIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from Claude Compliance, keyed by dataflow ID.
        :type dataflows: ClaudeComplianceIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Claude Compliance integration account.
        :type name: str
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
