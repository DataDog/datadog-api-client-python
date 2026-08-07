# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_git_hub_account_repository import CIAppGitHubAccountRepository


class CIAppGitHubAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_git_hub_account_repository import CIAppGitHubAccountRepository

        return {
            "account": (str,),
            "enabled": (bool,),
            "host": (str,),
            "repo_count": (int,),
            "repositories": ([CIAppGitHubAccountRepository],),
        }

    attribute_map = {
        "account": "account",
        "enabled": "enabled",
        "host": "host",
        "repo_count": "repo_count",
        "repositories": "repositories",
    }

    def __init__(
        self_,
        account: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        repo_count: Union[int, UnsetType] = unset,
        repositories: Union[List[CIAppGitHubAccountRepository], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes describing a GitHub account's CI Visibility opt-in status.

        :param account: The GitHub account (organization or user) name.
        :type account: str, optional

        :param enabled: Whether CI Visibility is enabled at the account level.
        :type enabled: bool, optional

        :param host: The GitHub host ( ``github.com`` or a GHES hostname) this account belongs to.
        :type host: str, optional

        :param repo_count: The number of repositories known for this account.
        :type repo_count: int, optional

        :param repositories: The repositories belonging to this account, with their individual opt-in status.
        :type repositories: [CIAppGitHubAccountRepository], optional
        """
        if account is not unset:
            kwargs["account"] = account
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if host is not unset:
            kwargs["host"] = host
        if repo_count is not unset:
            kwargs["repo_count"] = repo_count
        if repositories is not unset:
            kwargs["repositories"] = repositories
        super().__init__(kwargs)
