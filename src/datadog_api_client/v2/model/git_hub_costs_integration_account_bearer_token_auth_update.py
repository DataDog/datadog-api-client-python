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
    from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_type import (
        GitHubCostsIntegrationAccountBearerTokenAuthType,
    )


class GitHubCostsIntegrationAccountBearerTokenAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_type import (
            GitHubCostsIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (GitHubCostsIntegrationAccountBearerTokenAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(
        self_,
        auth_type: GitHubCostsIntegrationAccountBearerTokenAuthType,
        token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Bearer token authentication. For an enterprise, use a personal access token (classic) from an Enterprise Admin with the ``manage_billing:enterprise`` and ``read:org`` scopes. For an organization, use a fine-grained personal access token created by an organization owner, with the organization as resource owner and read-only ``Administration`` permission. Only the fields provided are changed; omit ``token`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: GitHubCostsIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with GitHub.
        :type token: str, optional
        """
        if token is not unset:
            kwargs["token"] = token
        super().__init__(kwargs)

        self_.auth_type = auth_type
