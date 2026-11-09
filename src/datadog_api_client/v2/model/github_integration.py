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
    from datadog_api_client.v2.model.github_credentials import GithubCredentials
    from datadog_api_client.v2.model.github_integration_type import GithubIntegrationType
    from datadog_api_client.v2.model.github_app import GithubApp
    from datadog_api_client.v2.model.github_personal_access_token import GithubPersonalAccessToken


class GithubIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.github_credentials import GithubCredentials
        from datadog_api_client.v2.model.github_integration_type import GithubIntegrationType

        return {
            "credentials": (GithubCredentials,),
            "type": (GithubIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        credentials: Union[GithubCredentials, GithubApp, GithubPersonalAccessToken],
        type: GithubIntegrationType,
        **kwargs,
    ):
        """
        GitHub connection integration.

        :param credentials: Supported GitHub connection credentials.
        :type credentials: GithubCredentials

        :param type: The GitHub integration type.
        :type type: GithubIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
