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
    from datadog_api_client.v2.model.synthetics_test_result_git_commit import SyntheticsTestResultGitCommit


class SyntheticsTestResultGit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_git_commit import SyntheticsTestResultGitCommit

        return {
            "branch": (str,),
            "commit": (SyntheticsTestResultGitCommit,),
            "repository_url": (str,),
        }

    attribute_map = {
        "branch": "branch",
        "commit": "commit",
        "repository_url": "repository_url",
    }

    def __init__(
        self_,
        branch: Union[str, UnsetType] = unset,
        commit: Union[SyntheticsTestResultGitCommit, UnsetType] = unset,
        repository_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Git information associated with the test result.

        :param branch: Git branch name.
        :type branch: str, optional

        :param commit: Details of the Git commit associated with the test result.
        :type commit: SyntheticsTestResultGitCommit, optional

        :param repository_url: Git repository URL.
        :type repository_url: str, optional
        """
        if branch is not unset:
            kwargs["branch"] = branch
        if commit is not unset:
            kwargs["commit"] = commit
        if repository_url is not unset:
            kwargs["repository_url"] = repository_url
        super().__init__(kwargs)
