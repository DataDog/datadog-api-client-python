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
    from datadog_api_client.v2.model.synthetics_test_result_git_user import SyntheticsTestResultGitUser


class SyntheticsTestResultGitCommit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_git_user import SyntheticsTestResultGitUser

        return {
            "author": (SyntheticsTestResultGitUser,),
            "committer": (SyntheticsTestResultGitUser,),
            "message": (str,),
            "sha": (str,),
            "url": (str,),
        }

    attribute_map = {
        "author": "author",
        "committer": "committer",
        "message": "message",
        "sha": "sha",
        "url": "url",
    }

    def __init__(
        self_,
        author: Union[SyntheticsTestResultGitUser, UnsetType] = unset,
        committer: Union[SyntheticsTestResultGitUser, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        sha: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the Git commit associated with the test result.

        :param author: A Git user (author or committer).
        :type author: SyntheticsTestResultGitUser, optional

        :param committer: A Git user (author or committer).
        :type committer: SyntheticsTestResultGitUser, optional

        :param message: Commit message.
        :type message: str, optional

        :param sha: Commit SHA.
        :type sha: str, optional

        :param url: URL of the commit.
        :type url: str, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if committer is not unset:
            kwargs["committer"] = committer
        if message is not unset:
            kwargs["message"] = message
        if sha is not unset:
            kwargs["sha"] = sha
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
