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
    from datadog_api_client.v2.model.git_hub_costs_integration_account_authentication_update import (
        GitHubCostsIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_update import (
        GitHubCostsIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_update import (
        GitHubCostsIntegrationAccountBearerTokenAuthUpdate,
    )


class GitHubCostsIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_costs_integration_account_authentication_update import (
            GitHubCostsIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_update import (
            GitHubCostsIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (GitHubCostsIntegrationAccountAuthenticationUpdate,),
            "name": (str,),
            "settings": (GitHubCostsIntegrationAccountSettingsUpdate,),
        }

    attribute_map = {
        "authentication": "authentication",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            GitHubCostsIntegrationAccountAuthenticationUpdate,
            GitHubCostsIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[GitHubCostsIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a GitHub Costs integration account. Every field is optional; only the fields provided are changed.

        :param authentication: Authentication for updating the GitHub Costs integration account. Exactly one method is set.
        :type authentication: GitHubCostsIntegrationAccountAuthenticationUpdate, optional

        :param name: Human-readable name of the GitHub Costs integration account.
        :type name: str, optional

        :param settings: Settings for updating the GitHub Costs integration account. Only the fields provided are changed.
        :type settings: GitHubCostsIntegrationAccountSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
