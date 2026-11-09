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
    from datadog_api_client.v2.model.github_app_github_app_id import GithubAppGithubAppId
    from datadog_api_client.v2.model.github_app_github_installation_id import GithubAppGithubInstallationId
    from datadog_api_client.v2.model.github_app_hostname import GithubAppHostname
    from datadog_api_client.v2.model.github_app_private_key import GithubAppPrivateKey
    from datadog_api_client.v2.model.github_app_type import GithubAppType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class GithubApp(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.github_app_github_app_id import GithubAppGithubAppId
        from datadog_api_client.v2.model.github_app_github_installation_id import GithubAppGithubInstallationId
        from datadog_api_client.v2.model.github_app_hostname import GithubAppHostname
        from datadog_api_client.v2.model.github_app_private_key import GithubAppPrivateKey
        from datadog_api_client.v2.model.github_app_type import GithubAppType

        return {
            "github_app_id": (GithubAppGithubAppId,),
            "github_installation_id": (GithubAppGithubInstallationId,),
            "hostname": (GithubAppHostname,),
            "private_key": (GithubAppPrivateKey,),
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
        github_app_id: Union[GithubAppGithubAppId, str, ActionConnectionAWSSecretsManagerReference],
        github_installation_id: Union[GithubAppGithubInstallationId, str, ActionConnectionAWSSecretsManagerReference],
        private_key: Union[GithubAppPrivateKey, str, ActionConnectionAWSSecretsManagerReference],
        type: GithubAppType,
        hostname: Union[GithubAppHostname, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        **kwargs,
    ):
        """
        GitHub App credentials.

        :param github_app_id: The numeric ID of the GitHub App.
        :type github_app_id: GithubAppGithubAppId

        :param github_installation_id: The installation ID of the GitHub App.
        :type github_installation_id: GithubAppGithubInstallationId

        :param hostname: Hostname of the GitHub Enterprise Server. Omit this field for github.com.
        :type hostname: GithubAppHostname, optional

        :param private_key: PEM-encoded RSA private key for the GitHub App.
        :type private_key: GithubAppPrivateKey

        :param type: The credential type for ``GithubApp``.
        :type type: GithubAppType
        """
        if hostname is not unset:
            kwargs["hostname"] = hostname
        super().__init__(kwargs)

        self_.github_app_id = github_app_id
        self_.github_installation_id = github_installation_id
        self_.private_key = private_key
        self_.type = type
