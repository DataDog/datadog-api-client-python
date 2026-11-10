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
    from datadog_api_client.v2.model.git_hub_costs_integration_account_authentication_response import (
        GitHubCostsIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_dataflows_response import (
        GitHubCostsIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_response import (
        GitHubCostsIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_response import (
        GitHubCostsIntegrationAccountBearerTokenAuthResponse,
    )


class GitHubCostsIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_costs_integration_account_authentication_response import (
            GitHubCostsIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.git_hub_costs_integration_dataflows_response import (
            GitHubCostsIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_response import (
            GitHubCostsIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (GitHubCostsIntegrationAccountAuthenticationResponse,),
            "dataflows": (GitHubCostsIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (GitHubCostsIntegrationAccountSettingsResponse,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        settings: GitHubCostsIntegrationAccountSettingsResponse,
        authentication: Union[
            GitHubCostsIntegrationAccountAuthenticationResponse,
            GitHubCostsIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[GitHubCostsIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a GitHub Costs integration account returned in responses.

        :param authentication: Authentication configured on the GitHub Costs integration account.
        :type authentication: GitHubCostsIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from GitHub Costs, keyed by dataflow id.
        :type dataflows: GitHubCostsIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the GitHub Costs integration account.
        :type name: str

        :param settings: Settings configured on the GitHub Costs integration account.
        :type settings: GitHubCostsIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
