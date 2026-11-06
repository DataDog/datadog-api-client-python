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
    from datadog_api_client.v2.model.github_credentials_update import GithubCredentialsUpdate
    from datadog_api_client.v2.model.github_integration_type import GithubIntegrationType
    from datadog_api_client.v2.model.github_app_update import GithubAppUpdate
    from datadog_api_client.v2.model.github_personal_access_token_update import GithubPersonalAccessTokenUpdate


class GithubIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.github_credentials_update import GithubCredentialsUpdate
        from datadog_api_client.v2.model.github_integration_type import GithubIntegrationType

        return {
            "credentials": (GithubCredentialsUpdate,),
            "type": (GithubIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: GithubIntegrationType,
        credentials: Union[
            GithubCredentialsUpdate, GithubAppUpdate, GithubPersonalAccessTokenUpdate, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        GitHub connection integration update.

        :param credentials: Supported GitHub connection credentials for an update.
        :type credentials: GithubCredentialsUpdate, optional

        :param type: The GitHub integration type.
        :type type: GithubIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
