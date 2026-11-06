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
    from datadog_api_client.v2.model.github_personal_access_token_update_access_token import (
        GithubPersonalAccessTokenUpdateAccessToken,
    )
    from datadog_api_client.v2.model.github_personal_access_token_update_hostname import (
        GithubPersonalAccessTokenUpdateHostname,
    )
    from datadog_api_client.v2.model.github_personal_access_token_type import GithubPersonalAccessTokenType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class GithubPersonalAccessTokenUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.github_personal_access_token_update_access_token import (
            GithubPersonalAccessTokenUpdateAccessToken,
        )
        from datadog_api_client.v2.model.github_personal_access_token_update_hostname import (
            GithubPersonalAccessTokenUpdateHostname,
        )
        from datadog_api_client.v2.model.github_personal_access_token_type import GithubPersonalAccessTokenType

        return {
            "access_token": (GithubPersonalAccessTokenUpdateAccessToken,),
            "hostname": (GithubPersonalAccessTokenUpdateHostname,),
            "type": (GithubPersonalAccessTokenType,),
        }

    attribute_map = {
        "access_token": "access_token",
        "hostname": "hostname",
        "type": "type",
    }

    def __init__(
        self_,
        type: GithubPersonalAccessTokenType,
        access_token: Union[
            GithubPersonalAccessTokenUpdateAccessToken, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        hostname: Union[
            GithubPersonalAccessTokenUpdateHostname, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Update to GitHub personal access token credentials.

        :param access_token: GitHub personal access token.
        :type access_token: GithubPersonalAccessTokenUpdateAccessToken, optional

        :param hostname: Hostname of the GitHub Enterprise Server. Omit this field for github.com.
        :type hostname: GithubPersonalAccessTokenUpdateHostname, optional

        :param type: The credential type for ``GithubPersonalAccessToken``.
        :type type: GithubPersonalAccessTokenType
        """
        if access_token is not unset:
            kwargs["access_token"] = access_token
        if hostname is not unset:
            kwargs["hostname"] = hostname
        super().__init__(kwargs)

        self_.type = type
