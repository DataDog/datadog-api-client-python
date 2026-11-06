# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GithubCredentials(ModelComposed):
    def __init__(self, **kwargs):
        """
        Supported GitHub connection credentials.

        :param github_app_id: The numeric ID of the GitHub App.
        :type github_app_id: GithubAppGithubAppId

        :param github_installation_id: The installation ID of the GitHub App.
        :type github_installation_id: GithubAppGithubInstallationId

        :param hostname: Hostname of the GitHub Enterprise Server. Omit this field for github.com.
        :type hostname: GithubAppHostname, optional

        :param private_key: PEM-encoded RSA private key for the GitHub App.
        :type private_key: GithubAppPrivateKey

        :param type: The credential type for `GithubApp`.
        :type type: GithubAppType

        :param access_token: GitHub personal access token.
        :type access_token: GithubPersonalAccessTokenAccessToken
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.github_app import GithubApp
        from datadog_api_client.v2.model.github_personal_access_token import GithubPersonalAccessToken

        return {
            "oneOf": [
                GithubApp,
                GithubPersonalAccessToken,
            ],
        }
