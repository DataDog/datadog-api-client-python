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
    from datadog_api_client.v2.model.github_app_update_github_app_id import GithubAppUpdateGithubAppId
    from datadog_api_client.v2.model.github_app_update_github_installation_id import GithubAppUpdateGithubInstallationId
    from datadog_api_client.v2.model.github_app_update_hostname import GithubAppUpdateHostname
    from datadog_api_client.v2.model.github_app_update_private_key import GithubAppUpdatePrivateKey
    from datadog_api_client.v2.model.github_app_type import GithubAppType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class GithubAppUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.github_app_update_github_app_id import GithubAppUpdateGithubAppId
        from datadog_api_client.v2.model.github_app_update_github_installation_id import (
            GithubAppUpdateGithubInstallationId,
        )
        from datadog_api_client.v2.model.github_app_update_hostname import GithubAppUpdateHostname
        from datadog_api_client.v2.model.github_app_update_private_key import GithubAppUpdatePrivateKey
        from datadog_api_client.v2.model.github_app_type import GithubAppType

        return {
            "github_app_id": (GithubAppUpdateGithubAppId,),
            "github_installation_id": (GithubAppUpdateGithubInstallationId,),
            "hostname": (GithubAppUpdateHostname,),
            "private_key": (GithubAppUpdatePrivateKey,),
            "type": (GithubAppType,),
        }

    attribute_map = {
        "github_app_id": "github_app_id",
        "github_installation_id": "github_installation_id",
        "hostname": "hostname",
        "private_key": "private_key",
        "type": "type",
    }

    def __init__(
        self_,
        type: GithubAppType,
        github_app_id: Union[
            GithubAppUpdateGithubAppId, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        github_installation_id: Union[
            GithubAppUpdateGithubInstallationId, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        hostname: Union[GithubAppUpdateHostname, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        private_key: Union[
            GithubAppUpdatePrivateKey, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Update to GitHub App credentials.

        :param github_app_id: The numeric ID of the GitHub App.
        :type github_app_id: GithubAppUpdateGithubAppId, optional

        :param github_installation_id: The installation ID of the GitHub App.
        :type github_installation_id: GithubAppUpdateGithubInstallationId, optional

        :param hostname: Hostname of the GitHub Enterprise Server. Omit this field for github.com.
        :type hostname: GithubAppUpdateHostname, optional

        :param private_key: PEM-encoded RSA private key for the GitHub App.
        :type private_key: GithubAppUpdatePrivateKey, optional

        :param type: The credential type for ``GithubApp``.
        :type type: GithubAppType
        """
        if github_app_id is not unset:
            kwargs["github_app_id"] = github_app_id
        if github_installation_id is not unset:
            kwargs["github_installation_id"] = github_installation_id
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if private_key is not unset:
            kwargs["private_key"] = private_key
        super().__init__(kwargs)

        self_.type = type
