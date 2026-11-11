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
    from datadog_api_client.v2.model.git_hub_costs_integration_account_authentication_request import (
        GitHubCostsIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_request import (
        GitHubCostsIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_request import (
        GitHubCostsIntegrationAccountBearerTokenAuthRequest,
    )


class GitHubCostsIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_costs_integration_account_authentication_request import (
            GitHubCostsIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_request import (
            GitHubCostsIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (GitHubCostsIntegrationAccountAuthenticationRequest,),
            "name": (str,),
            "settings": (GitHubCostsIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            GitHubCostsIntegrationAccountAuthenticationRequest, GitHubCostsIntegrationAccountBearerTokenAuthRequest
        ],
        name: str,
        settings: GitHubCostsIntegrationAccountSettingsRequest,
        **kwargs,
    ):
        """
        Writable attributes used to create a GitHub Costs integration account.

        :param authentication: Authentication for creating the GitHub Costs integration account. Exactly one method is set.
        :type authentication: GitHubCostsIntegrationAccountAuthenticationRequest

        :param name: Human-readable name of the GitHub Costs integration account.
        :type name: str

        :param settings: Settings for creating the GitHub Costs integration account.
        :type settings: GitHubCostsIntegrationAccountSettingsRequest
        """
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
